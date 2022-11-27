import unittest

from antlr4.error.Errors import ParseCancellationException
from commands.command_visitor import CommandVisitor
from commands.exceptions.redirection_error import RedirectionError
from commands.impl.call import Call
from commands.impl.pipe import Pipe
from commands.impl.seq import Seq
import os
import shutil


class TestCommandVisitor(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = "resources"
        os.mkdir(self.temp_dir)
        self.paths = dict()

        self.files = {
            "test1.txt": "",
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_seq(self):
        cmdline = "echo hello ; echo world"
        command = CommandVisitor.parse(cmdline)
        expected = Seq(
            Call("echo", ["hello"], None, None),
            Call("echo", ["world"], None, None)
        )
        self.assertEqual(command, expected)

    def test_nested_seq(self):
        cmdline = "echo hello ; echo world ; cat test1.txt"
        command = CommandVisitor.parse(cmdline)
        expected = Seq(
            Seq(
                Call("echo", ["hello"], None, None),
                Call("echo", ["world"], None, None)
            ),
            Call("cat", ["test1.txt"], None, None)
        )
        self.assertEqual(command, expected)

    def test_single_pipe(self):
        cmdline = "cat test1.txt | grep Interesting"
        command = CommandVisitor.parse(cmdline)
        expected = Pipe(
            Call("cat", ["test1.txt"], None, None),
            Call("grep", ["Interesting"], None, None)
        )
        self.assertEqual(command, expected)

    def test_nested_pipe(self):
        cmdline = "echo Interesting | grep Int | grep ing"
        command = CommandVisitor.parse(cmdline)
        expected = Pipe(
            Pipe(
                Call("echo", ["Interesting"], None, None),
                Call("grep", ["Int"], None, None)
            ),
            Call("grep", ["ing"], None, None)
        )
        self.assertEqual(command, expected)

    def test_input_redirection(self):
        cmdline = "cat < test1.txt"
        command = CommandVisitor.parse(cmdline)
        expected = Call("cat", [], "test1.txt", None)
        self.assertEqual(command, expected)

    def test_output_redirection(self):
        cmdline = "echo hello > test1.txt"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["hello"], None, "test1.txt")
        self.assertEqual(command, expected)

    def test_redirection_in_front(self):
        cmdline = "< test1.txt cat"
        command = CommandVisitor.parse(cmdline)
        expected = Call("cat", [], "test1.txt", None)
        self.assertEqual(command, expected)

    def test_globbing(self):
        cmdline = f"echo {self.temp_dir}/*"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", [self.paths["test1.txt"]], None, None)
        self.assertEqual(command, expected)

    def test_globbing_argument_splitting(self):
        cmdline = f"echo `echo a {self.temp_dir}/`*"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["a", self.paths["test1.txt"]], None, None)
        self.assertEqual(command, expected)

    def test_globbing_no_matches(self):
        cmdline = f"echo {self.temp_dir}/a/*"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", [f"{self.temp_dir}/a/*"], None, None)
        self.assertEqual(command, expected)

    def test_unquoted(self):
        cmdline = "echo hello"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["hello"], None, None)
        self.assertEqual(command, expected)

    def test_single_quoted(self):
        cmdline = "echo 'Interesting String'"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["Interesting String"], None, None)
        self.assertEqual(command, expected)

    def test_single_quoted_backquoted(self):
        cmdline = "echo 'hello `echo a`'"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["hello `echo a`"], None, None)
        self.assertEqual(command, expected)

    def test_single_quoted_disabled_globbing(self):
        cmdline = "echo 'hello*'"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["hello*"], None, None)
        self.assertEqual(command, expected)

    def test_backquoted(self):
        cmdline = "echo `echo hello`"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["hello"], None, None)
        self.assertEqual(command, expected)

    def test_backquoted_disabled_globbing(self):
        cmdline = "echo `echo 'hello*'`"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["hello*"], None, None)
        self.assertEqual(command, expected)

    def test_backquoted_argument_splitting(self):
        cmdline = "echo `echo hello world`"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["hello", "world"], None, None)
        self.assertEqual(command, expected)

    def test_double_quoted(self):
        cmdline = 'echo "Interesting String"'
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["Interesting String"], None, None)
        self.assertEqual(command, expected)

    def test_double_quoted_backquoted(self):
        cmdline = 'echo "hello `echo a`"'
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["hello a "], None, None)
        self.assertEqual(command, expected)

    def test_double_quoted_disabled_globbing(self):
        cmdline = 'echo "hello*"'
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["hello*"], None, None)
        self.assertEqual(command, expected)

    def test_parse_cancellation_exception(self):
        cmdline = "echo '"
        with self.assertRaises(ParseCancellationException):
            CommandVisitor.parse(cmdline)

    def test_several_input_redirections_error(self):
        cmdline = "cat < test1.txt < test2.txt"
        with self.assertRaises(RedirectionError):
            CommandVisitor.parse(cmdline)

    def test_several_output_redirections_error(self):
        cmdline = "echo hello > test1.txt > test2.txt"
        with self.assertRaises(RedirectionError):
            CommandVisitor.parse(cmdline)

    def test_several_redirection_files_error(self):
        cmdline = "cat < `echo test1.txt test2.txt`"
        with self.assertRaises(RedirectionError):
            CommandVisitor.parse(cmdline)
