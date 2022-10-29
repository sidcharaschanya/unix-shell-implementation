import unittest

from shell import eval
from collections import deque
import os


class TestShell(unittest.TestCase):
    def test_cat(self):
        out = deque()
        eval("cat dir1/test1.txt dir1/test2.txt", out)
        self.assertEqual(list(out), ["hello\n", "hehehehe\nhellohello\n"])

    def test_cat_empty_file(self):
        out = deque()
        eval("cat dir1/empty_file.txt", out)
        self.assertEqual(out.popleft(), "")
        self.assertEqual(len(out), 0)

    def test_cat_zero_args(self):
        self.assertRaises(ValueError, eval, "cat", deque())

    def test_cat_stdin(self):
        pass

    def test_cd(self):
        cwd = os.getcwd()
        eval("cd dir1", deque())
        self.assertEqual(os.getcwd(), os.path.join(cwd, "dir1"))
        os.chdir(cwd)

    def test_cd_zero_args(self):
        self.assertRaises(ValueError, eval, "cd", deque())

    def test_echo(self):
        out = deque()
        eval("echo hello world", out)
        self.assertEqual(out.popleft(), "hello world\n")
        self.assertEqual(len(out), 0)

    def test_echo_nothing(self):
        out = deque()
        eval("echo", out)
        self.assertEqual(out.popleft(), "\n")
        self.assertEqual(len(out), 0)

    def test_find_zero_args(self):
        self.assertRaises(ValueError, eval, "find", deque())

    def test_grep(self):
        out = deque()
        eval("grep he dir1/test1.txt", out)
        self.assertEqual(out.popleft(), "hello\n")
        self.assertEqual(len(out), 0)

    def test_grep_multiple_files(self):
        out = deque()
        eval("grep he dir1/test2.txt dir1/test1.txt", out)
        result = list(out)
        self.assertEqual(result, [
            "dir1/test2.txt:hehehehe\n",
            "dir1/test2.txt:hellohello\n",
            "dir1/test1.txt:hello\n"
        ])

    def test_grep_no_matches(self):
        out = deque()
        eval("grep aa dir1/test1.txt", out)
        self.assertEqual(len(out), 0)

    def test_pwd(self):
        out = deque()
        eval("pwd", out)
        self.assertEqual(out.popleft(), os.getcwd())
        self.assertEqual(len(out), 0)

    def test_pwd_one_arg(self):
        self.assertRaises(ValueError, eval, "pwd arg", deque())

    def test_sort(self):
        out = deque()
        eval("sort dir1/sort_test_file.txt", out)
        result = list(out)
        self.assertEqual(result, ["aaa\n", "hello world\n"])

    def test_sort_r(self):
        out = deque()
        eval("sort -r dir1/sort_test_file.txt", out)
        result = list(out)
        self.assertEqual(result, ["hello world\n", "aaa\n"])

    def test_uniq(self):
        out = deque()
        eval("uniq dir1/uniq_test_file.txt", out)
        result = list(out)
        self.assertEqual(result, ["aaa\n", "AAA\n", "aaa\n"])

    def test_uniq_i(self):
        out = deque()
        eval("uniq -i dir1/uniq_test_file.txt", out)
        result = list(out)
        self.assertEqual(result, ["aaa\n"])

    def test_uniq_empty_file(self):
        out = deque()
        eval("uniq dir1/empty_file.txt", out)
        result = list(out)
        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()
