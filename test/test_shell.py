import unittest

from shell import eval
from collections import deque
import os


class TestShell(unittest.TestCase):
    def test_shell(self):
        out = deque()
        eval("echo foo", out)
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)

    def testCd(self):
        out = deque()
        #print('testing cd')
        args = 'COMP0010'
        c = cd.Cd()
        c.exec(args,None,out)
        #self.assertIsNotNone(args)
        self.assertEqual(out,'COMP0010')

    def testHead(self):
        os.chdir('COMP0010')
        out = deque()
        current_dir = os.getcwd()
        args = ["requirements.txt"]
        h = head.Head()
        h.exec(args, None, out)
        #self.assertIsNotNone(current_dir)
        data = "nose2\ncoverage\nflake8==3.8.0\nflake8-html\njunit2html"
        self.assertEqual(out, data)


if __name__ == "__main__":
    unittest.main()
