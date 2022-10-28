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

    def testGrep_multipleFiles(self):
        out=deque()
        eval("grep he test2 test",out)
        result=list(out)
        self.assertEqual(result,["test2:hehehehe\n","test2:hellohello\n","test:hello\n"])

    def testGrep_noMatches(self):
        out=deque()
        eval("grep aa test",out)
        self.assertEqual(len(out),0)

    def test_sort(self):
        out=deque()
        eval("sort test2",out)
        result=list(out)
        self.assertEqual(result,["aaa\n","hello world\n"])

    def test_sort_r(self):
        out=deque()
        eval("sort -r test2",out)
        result=list(out)
        self.assertEqual(result,["hello world\n","aaa\n"])



if __name__ == "__main__":
    unittest.main()
