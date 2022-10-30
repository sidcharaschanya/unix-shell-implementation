import unittest

from shell import eval
from collections import deque
import os


class TestShell(unittest.TestCase):
    def test_cat(self):
        out = deque()
        eval("cat resources/dir1/test1.txt resources/dir1/test2.txt", out)
        self.assertEqual(set(out), {"hello\n", "hehehehe\nhellohello\n"})

    def test_cat_empty_file(self):
        out = deque()
        eval("cat resources/dir1/empty_file.txt", out)
        self.assertEqual(out.popleft(), "")
        self.assertEqual(len(out), 0)

    def cat_stdin(self):
        pass

    def test_cat_zero_args_invalid(self):
        self.assertRaises(ValueError, eval, "cat", deque())

    def test_cd(self):
        cwd = os.getcwd()
        eval("cd resources/dir1", deque())
        self.assertEqual(os.getcwd(), os.path.join(cwd, "resources/dir1"))
        os.chdir(cwd)

    def test_cd_zero_args_invalid(self):
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

    def test_find(self):
        out = deque()
        eval("find -name resources/dir2/file.txt", out)
        self.assertEqual(out.popleft(), "resources/dir2/file.txt\n")
        self.assertEqual(len(out), 0)

    def test_find_pattern(self):
        out = deque()
        eval("find -name empty*", out)
        self.assertEqual(set(out), {"resources/empty_dir\n", "resources/dir1/empty_file.txt\n"})

    def test_find_path(self):
        out = deque()
        eval("find resources/dir2 -name *.txt", out)
        self.assertEqual(set(out), {"resources/dir2/file.txt\n", "resources/dir2/sub_dir/sub_file.txt\n"})

    def test_find_empty_dir(self):
        out = deque()
        eval("find resources/empty_dir -name *", out)
        self.assertEqual(len(out), 0)

    def test_find_no_matches(self):
        out = deque()
        eval("find resources/dir2 -name *.py", out)
        self.assertEqual(len(out), 0)

    def test_find_zero_args_invalid(self):
        self.assertRaises(ValueError, eval, "find", deque())

    def test_find_two_args_invalid(self):
        self.assertRaises(ValueError, eval, "find arg0 arg1", deque())

    def test_find_three_args_invalid(self):
        self.assertRaises(ValueError, eval, "find arg0 arg1 arg2", deque())

    def test_grep(self):
        out = deque()
        eval("grep he resources/dir1/test1.txt", out)
        self.assertEqual(out.popleft(), "hello\n")
        self.assertEqual(len(out), 0)

    def test_grep_multiple_files(self):
        out = deque()
        eval("grep he resources/dir1/test2.txt resources/dir1/test1.txt", out)
        result = set(out)
        self.assertEqual(result, {
            "resources/dir1/test2.txt:hehehehe\n",
            "resources/dir1/test2.txt:hellohello\n",
            "resources/dir1/test1.txt:hello\n"
        })

    def test_grep_no_matches(self):
        out = deque()
        eval("grep aa resources/dir1/test1.txt", out)
        self.assertEqual(len(out), 0)

    def test_grep_stdin(self):
        pass

    def test_head(self):
        out = deque()
        eval("head resources/dir1/test3.txt", out)
        self.assertEqual(set(out), {str(i) + "\n" for i in range(9)})

    def test_head_num_lines(self):
        out = deque()
        eval("head -n 5 resources/dir1/test3.txt", out)
        self.assertEqual(set(out), {str(i) + "\n" for i in range(5)})

    def test_head_stdin(self):
        pass

    def test_head_stdin_num_lines(self):
        pass

    def test_head_empty_file(self):
        out = deque()
        eval("head resources/dir1/empty_file.txt", out)
        self.assertEqual(len(out), 0)

    def test_head_zero_lines(self):
        out = deque()
        eval("head -n 0 resources/dir1/test3.txt", out)
        self.assertEqual(len(out), 0)

    def test_head_zero_args_invalid(self):
        self.assertRaises(ValueError, eval, "head", deque())

    def test_head_two_args_wrong_flags(self):
        self.assertRaises(ValueError, eval, "head arg0 arg1", deque())

    def test_head_two_args_no_stdin(self):
        self.assertRaises(ValueError, eval, "head -n arg1", deque())

    def test_head_three_args_invalid(self):
        self.assertRaises(ValueError, eval, "head arg0 arg1 arg2", deque())

    def test_head_four_args_invalid(self):
        self.assertRaises(ValueError, eval, "head arg0 arg1 arg2 arg3", deque())

    def test_ls(self):
        cwd = os.getcwd()
        os.chdir("resources/dir2")
        out = deque()
        eval("ls", out)
        self.assertEqual(set(out), {"file.txt\n", "sub_dir\n"})
        os.chdir(cwd)

    def test_ls_path(self):
        out = deque()
        eval("ls resources/dir2", out)
        self.assertEqual(set(out), {"file.txt\n", "sub_dir\n"})

    def test_ls_empty_dir(self):
        out = deque()
        eval("ls resources/empty_dir", out)
        self.assertEqual(len(out), 0)

    def test_ls_two_args_invalid(self):
        self.assertRaises(ValueError, eval, "ls arg0 arg1", deque())

    def test_pwd(self):
        out = deque()
        eval("pwd", out)
        self.assertEqual(out.popleft(), os.getcwd())
        self.assertEqual(len(out), 0)

    def test_pwd_one_arg(self):
        self.assertRaises(ValueError, eval, "pwd arg", deque())

    def test_sort(self):
        out = deque()
        eval("sort resources/dir1/sort_test_file.txt", out)
        result = set(out)
        self.assertEqual(result, {"aaa\n", "hello world\n"})

    def test_sort_r(self):
        out = deque()
        eval("sort -r resources/dir1/sort_test_file.txt", out)
        result = set(out)
        self.assertEqual(result, {"hello world\n", "aaa\n"})

    def test_sort_stdin(self):
        pass

    def test_tail(self):
        out = deque()
        eval("tail resources/dir1/test3.txt", out)
        self.assertEqual(set(out), {str(i) + "\n" for i in range(9)})

    def test_tail_num_lines(self):
        out = deque()
        eval("tail -n 5 resources/dir1/test3.txt", out)
        self.assertEqual(set(out), {str(i) + "\n" for i in range(4, 9)})

    def test_tail_stdin(self):
        pass

    def test_tail_stdin_num_lines(self):
        pass

    def test_tail_empty_file(self):
        out = deque()
        eval("tail resources/dir1/empty_file.txt", out)
        self.assertEqual(len(out), 0)

    def test_tail_zero_lines(self):
        out = deque()
        eval("tail -n 0 resources/dir1/test3.txt", out)
        self.assertEqual(len(out), 0)

    def test_tail_zero_args_invalid(self):
        self.assertRaises(ValueError, eval, "tail", deque())

    def test_tail_two_args_wrong_flags(self):
        self.assertRaises(ValueError, eval, "tail arg0 arg1", deque())

    def test_tail_two_args_no_stdin(self):
        self.assertRaises(ValueError, eval, "tail -n arg1", deque())

    def test_tail_three_args_invalid(self):
        self.assertRaises(ValueError, eval, "tail arg0 arg1 arg2", deque())

    def test_tail_four_args_invalid(self):
        self.assertRaises(ValueError, eval, "tail arg0 arg1 arg2 arg3", deque())

    def test_uniq(self):
        out = deque()
        eval("uniq resources/dir1/uniq_test_file.txt", out)
        result = set(out)
        self.assertEqual(result, {"aaa\n", "AAA\n", "aaa\n"})

    def test_uniq_i(self):
        out = deque()
        eval("uniq -i resources/dir1/uniq_test_file.txt", out)
        result = set(out)
        self.assertEqual(result, {"aaa\n"})

    def test_uniq_empty_file(self):
        out = deque()
        eval("uniq resources/dir1/empty_file.txt", out)
        result = set(out)
        self.assertEqual(len(result), 0)

    def test_unsafe_ls(self):
        out = deque()
        eval("_ls dir0", out)
        self.assertEqual(len(out), 0)


if __name__ == "__main__":
    unittest.main()
