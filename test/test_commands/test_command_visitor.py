import os
import shutil
import unittest
from collections import deque

from commands.command_visitor import CommandVisitor
from commands.impl.seq import Seq
from commands.impl.call import Call
from commands.impl.pipe import Pipe

class TestCommandVisitor(unittest.TestCase):

    def setUp(self) -> None:
        self.out = deque()
        self.temp_dir = "resources"
        os.mkdir(self.temp_dir)
        self.paths = dict()

        self.files = {
            "test1.txt": "hello\n",
            #"test2.txt": "hehehehe\nhellohello\n",
            #"empty_file.txt": ""
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_seq_command(self):
            cmdline="echo hello;echo hi"
            command=CommandVisitor.parse(cmdline)
            expected=Seq(Call("echo",["hello"],None,None),Call("echo",["hi"],None,None))
            self.assertEqual(command,expected)

    def test_nested_seq(self):
        cmdline="echo hello; echo hi; cat test.txt"
        command=CommandVisitor.parse(cmdline)
        expected=Seq(Seq(Call("echo",["hello"],None,None),Call("echo",["hi"],None,None)),Call("cat",["test.txt"],None,None))
        self.assertEqual(command, expected)

    def test_pipe(self):
        cmdline="cat test.txt | grep 'Interesting String'"
        command=CommandVisitor.parse(cmdline)
        expected=Pipe(Call("cat",["test.txt"],None,None),Call("grep",["Interesting String"],None,None))
        self.assertEqual(command, expected)

    def test_nested_pipe(self):
        cmdline="echo 'Interesting String' | grep 'Interesting String' | grep 'Ie'"
        command=CommandVisitor.parse(cmdline)
        expected=Pipe(Pipe(Call("echo",['Interesting String'],None,None),Call("grep",["Interesting String"],None,None)),Call("grep",["Ie"],None,None))
        self.assertEqual(command, expected)

    def test_single_quote(self):
        cmdline = "echo 'Interesting String'"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo",['Interesting String'],None,None)
        self.assertEqual(command,expected)

    # extra whitespace being added to the parsed command in double quotes even though the ANTLR displays it correctly
    # in test 2 and test 3

    def test_double_quotes(self):
        cmdline = 'echo "Interesting String"'
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ['Interesting String'], None, None)
        self.assertEqual(command, expected)

    def test_double_quotes_2(self):
        cmdline = 'echo "this is space: `echo " "`"'
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo",['this is space: '],None,None)
        self.assertEqual(command,expected)

    def test_double_quotes_3(self):
        cmdline = 'echo "hello `echo "a"`"'
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo", ['hello a'], None, None)
        self.assertEqual(command, expected)

    def test_back_quotes(self):
        pass

    def test_unquoted(self):
        cmdline = "echo hello"
        command = CommandVisitor.parse(cmdline)
        expected = Call("echo",['hello'],None,None)
        self.assertEqual(command,expected)

    #def test_


