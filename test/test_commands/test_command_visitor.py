import unittest
from commands.command_visitor import CommandVisitor
from commands.impl.seq import Seq
from commands.impl.call import Call
from commands.impl.pipe import Pipe

class TestCommandVisitor(unittest.TestCase):

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
        cmdline="echo 'Interesting String' > test.txt | cat test.txt | grep 'Interesting String'"
        command=CommandVisitor.parse(cmdline)
        expected=Pipe(Pipe(Call("echo",['Interesting String'],None,"test.txt"),Call("cat",["test.txt"],None,None)),Call("grep",["Interesting String"],None,None))
        self.assertEqual(command, expected)
