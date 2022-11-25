import unittest

from commands.command_visitor import CommandVisitor
from commands.impl.call import Call
from commands.impl.pipe import Pipe
from commands.impl.seq import Seq


class TestCommandVisitor(unittest.TestCase):
    def test_redirection_output(self):
        cmdline = "echo hello > test1.txt"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ["hello"], None, "test1.txt")
        self.assertEqual(command, expected)

    def test_redirection_input(self):
        cmdline = "cat < test1.txt"
        command = CommandVisitor.parse(cmdline)
        expected = Call("cat", [], "test1.txt", None)
        self.assertEqual(command, expected)

    def test_seq_command(self):
        cmdline = "echo hello;echo hi"
        command = CommandVisitor.parse(cmdline)
        expected = Seq(Call("echo", ["hello"], None, None), Call("echo", ["hi"], None, None))
        self.assertEqual(command, expected)

    def test_nested_seq(self):
        cmdline = "echo hello; echo hi; cat test1.txt"
        command = CommandVisitor.parse(cmdline)
        expected = Seq(Seq(Call("echo", ["hello"], None, None), Call("echo", ["hi"], None, None)),
                       Call("cat", ["test1.txt"], None, None))
        self.assertEqual(command, expected)

    def test_pipe(self):
        cmdline = "cat test1.txt | grep 'Interesting String'"
        command = CommandVisitor.parse(cmdline)
        expected = Pipe(Call("cat", ["test1.txt"], None, None), Call("grep", ["Interesting String"], None, None))
        self.assertEqual(command, expected)

    def test_nested_pipe(self):
        cmdline = "echo 'Interesting String' | grep 'Interesting String' | grep 'Ie'"
        command = CommandVisitor.parse(cmdline)
        expected = Pipe(
            Pipe(Call("echo", ['Interesting String'], None, None), Call("grep", ["Interesting String"], None, None)),
            Call("grep", ["Ie"], None, None))
        self.assertEqual(command, expected)

    def test_single_quote(self):
        cmdline = "echo 'Interesting String'"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ['Interesting String'], None, None)
        self.assertEqual(command, expected)

    def test_single_quote_with_back_quotes(self):
        cmdline = "echo 'hello `echo a`'"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ['hello `echo a`'], None, None)
        self.assertEqual(command, expected)

    def test_double_quotes(self):
        cmdline = 'echo "Interesting String"'
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ['Interesting String'], None, None)
        self.assertEqual(command, expected)

    def test_double_quotes_with_back_quotes(self):
        cmdline = 'echo "hello `echo "a"`"'
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ['hello a '], None, None)
        self.assertEqual(command, expected)

    def test_unquoted(self):
        cmdline = "echo hello"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ['hello'], None, None)
        self.assertEqual(command, expected)
