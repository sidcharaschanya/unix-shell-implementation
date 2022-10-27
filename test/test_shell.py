import unittest

from shell import eval
from collections import deque


class TestShell(unittest.TestCase):
    def test_shell(self):
        out = deque()
        eval("echo foo", out)
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)

    def testEcho(self):
        def test(self):
            out = deque()
            args = ["hello", "world"]
            e = echo.Echo()
            echo.exec(args, None, out)
            self.assertEqual(out.popleft(), "hello world\n")
            self.assertEqual(len(out), 0)

    def testGrep(self):
        out = deque()
        g = grep.Grep()

        args = ["he", "test"]
        g.exec(args, None, out)
        self.assertEqual(out.popleft(), "hello\n")

        self.assertEqual(len(out), 0)

        args = ["he"]
        stdin = ["hehehe", "hie", "hello"]
        g.exec(args, stdin, out)
        self.assertEqual(out.popleft(), "hehehe")
        self.assertEqual(out.popleft(), "hello")

        args = ["he", "test2", "test"]
        g.exec(args, None, out)
        self.assertEqual(out.popleft(), "test2:hehehehe\n")


if __name__ == "__main__":
    unittest.main()
