import unittest
from collections import deque
from commands.command_visitor import CommandVisitor
from commands.impl.call import Call

class TestCall(unittest.TestCase):
    def setUp(self) -> None:
        self.out=deque()

    def test_call(self):
        call=Call("echo",["hello"],None,None)
        call.eval(None,self.out)
        self.assertEqual(self.out.popleft(),"hello\n")
