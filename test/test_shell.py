import unittest

from shell import eval
from collections import deque
import os


class TestShell(unittest.TestCase):
    def test_ls(self):
        cwd = os.getcwd()
        os.chdir("res/dir2")
        out = deque()
        eval("ls", out)
        self.assertEqual(set(out), {"file.txt\t", "sub_dir\t", "\n"})
        os.chdir(cwd)

    def test_ls_path(self):
        out = deque()
        eval("ls res/dir2", out)
        self.assertEqual(set(out), {"file.txt\t", "sub_dir\t", "\n"})

    def test_ls_empty_dir(self):
        out = deque()
        eval("ls res/empty_dir", out)
        self.assertEqual(out.popleft(), "\n")
        self.assertEqual(len(out), 0)

    def test_ls_two_args_invalid(self):
        self.assertRaises(ValueError, eval, "ls arg0 arg1", deque())

    def test_pwd(self):
        out = deque()
        eval("pwd", out)
        self.assertEqual(out.popleft(), os.getcwd() + "\n")
        self.assertEqual(len(out), 0)

    def test_pwd_one_arg_invalid(self):
        self.assertRaises(ValueError, eval, "pwd arg", deque())

    def test_sort(self):
        out = deque()
        eval("sort res/dir1/test4.txt", out)
        self.assertEqual(list(out), ["aaa\n", "hello world\n"])

    def test_sort_reverse(self):
        out = deque()
        eval("sort -r res/dir1/test4.txt", out)
        self.assertEqual(list(out), ["hello world\n", "aaa\n"])

    def test_sort_stdin(self):
        pass

    def test_sort_stdin_reverse(self):
        pass

    def test_sort_empty_file(self):
        out = deque()
        eval("sort res/dir1/empty_file.txt", out)
        self.assertEqual(len(out), 0)

    def test_sort_empty_file_reverse(self):
        out = deque()
        eval("sort -r res/dir1/empty_file.txt", out)
        self.assertEqual(len(out), 0)

    def test_sort_zero_args_invalid(self):
        self.assertRaises(ValueError, eval, "sort", deque())

    def test_sort_one_arg_no_stdin(self):
        self.assertRaises(ValueError, eval, "sort -r", deque())

    def test_sort_one_arg_file_not_found(self):
        self.assertRaises(FileNotFoundError, eval, "sort res/file.txt", deque())

    def test_sort_two_args_wrong_flags(self):
        self.assertRaises(ValueError, eval, "sort arg0 arg1", deque())

    def test_sort_two_args_file_not_found(self):
        self.assertRaises(FileNotFoundError, eval, "sort -r res/file.txt", deque())

    def test_sort_three_args_invalid(self):
        self.assertRaises(ValueError, eval, "sort arg0 arg1 arg2", deque())

    def test_uniq(self):
        out = deque()
        eval("uniq res/dir1/test5.txt", out)
        self.assertEqual(list(out), ["aaa\n", "AAA\n", "aaa\n"])

    def test_uniq_ignore_case(self):
        out = deque()
        eval("uniq -i res/dir1/test5.txt", out)
        self.assertEqual(list(out), ["aaa\n"])

    def test_uniq_stdin(self):
        pass

    def test_uniq_stdin_ignore_case(self):
        pass

    def test_uniq_empty_file(self):
        out = deque()
        eval("uniq res/dir1/empty_file.txt", out)
        self.assertEqual(len(out), 0)

    def test_uniq_empty_file_ignore_case(self):
        out = deque()
        eval("uniq -i res/dir1/empty_file.txt", out)
        self.assertEqual(len(out), 0)

    def test_uniq_zero_args_invalid(self):
        self.assertRaises(ValueError, eval, "uniq", deque())

    def test_uniq_one_arg_no_stdin(self):
        self.assertRaises(ValueError, eval, "uniq -i", deque())

    def test_uniq_one_arg_file_not_found(self):
        self.assertRaises(FileNotFoundError, eval, "uniq res/file.txt", deque())

    def test_uniq_two_args_wrong_flags(self):
        self.assertRaises(ValueError, eval, "uniq arg0 arg1", deque())

    def test_uniq_two_args_file_not_found(self):
        self.assertRaises(FileNotFoundError, eval, "uniq -i res/file.txt", deque())

    def test_uniq_three_args_invalid(self):
        self.assertRaises(ValueError, eval, "uniq arg0 arg1 arg2", deque())

    def test_cut_normal(self):
        out = deque()
        eval("cut -b 1,2,3 res/dir1/test6.txt", out)
        self.assertEqual(list(out), ["hel\n", "aaa\n", "bbb\n"])

    def test_cut_pattern2(self):
        out = deque()
        eval("cut -b 1-3,5-7 res/dir1/test6.txt", out)
        self.assertEqual(list(out), ["helo w\n", "aaa\n", "bbbccc\n"])

    def test_cut_pattern3(self):
        out = deque()
        eval("cut -b -3,6- res/dir1/test6.txt", out)
        self.assertEqual(list(out), ["hel world\n", "aaa\n", "bbbcc\n"])

    def test_cut_overlap(self):
        out = deque()
        eval("cut -b 2-,3- res/dir1/test6.txt", out)
        self.assertEqual(list(out), ["ello world\n", "aa\n", "bb ccc\n"])
