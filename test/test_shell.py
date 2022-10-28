import unittest
from src.applications.impl import *

from shell import eval
from collections import deque


class TestShell(unittest.TestCase):
    def test_shell(self):
        out = deque()
        eval("echo foo", out)
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)

    def testEcho(self):
            out = deque()
            eval("echo hello world",out)
            self.assertEqual(out.popleft(), "hello world\n")
            self.assertEqual(len(out), 0)

    def testGrep(self):
        out = deque()
        
        eval("grep he test",out)
        self.assertEqual(out.popleft(), "hello\n")
        self.assertEqual(len(out), 0)




if __name__ == "__main__":
    unittest.main()
