import unittest

from shell import eval
from collections import deque
import os


class TestShell(unittest.TestCase):
    def test_cd(self):
        cwd = os.getcwd()
        eval("cd res/dir1", deque())
        self.assertEqual(os.getcwd(), os.path.join(cwd, "res/dir1"))
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
        eval("find -name res/dir2/file.txt", out)
        self.assertEqual(out.popleft(), "./res/dir2/file.txt\n")
        self.assertEqual(len(out), 0)

    def test_find_pattern(self):
        out = deque()
        eval("find -name res/empty*", out)
        self.assertEqual(out.popleft(), "./res/empty_dir\n")
        self.assertEqual(len(out), 0)

    def test_find_path(self):
        out = deque()
        eval("find res/dir2 -name *.txt", out)
        self.assertEqual(set(out), {"res/dir2/file.txt\n", "res/dir2/sub_dir/sub_file.txt\n"})

    def test_find_empty_dir(self):
        out = deque()
        eval("find res/empty_dir -name *", out)
        self.assertEqual(len(out), 0)

    def test_find_no_matches(self):
        out = deque()
        eval("find res/dir2 -name *.py", out)
        self.assertEqual(len(out), 0)

    def test_find_zero_args_invalid(self):
        self.assertRaises(ValueError, eval, "find", deque())

    def test_find_two_args_invalid(self):
        self.assertRaises(ValueError, eval, "find arg0 arg1", deque())

    def test_find_three_args_invalid(self):
        self.assertRaises(ValueError, eval, "find arg0 arg1 arg2", deque())

    def test_grep(self):
        out = deque()
        eval("grep he res/dir1/test1.txt", out)
        self.assertEqual(out.popleft(), "hello\n")
        self.assertEqual(len(out), 0)

    def test_grep_multiple_files(self):
        out = deque()
        eval("grep he res/dir1/test1.txt res/dir1/test2.txt", out)
        result = list(out)
        self.assertEqual(result, [
            "res/dir1/test1.txt:hello\n",
            "res/dir1/test2.txt:hehehehe\n",
            "res/dir1/test2.txt:hellohello\n",
        ])

    def test_grep_empty_file(self):
        out = deque()
        eval("grep aa res/dir1/empty_file.txt", out)
        self.assertEqual(len(out), 0)

    def test_grep_no_matches(self):
        out = deque()
        eval("grep aa res/dir1/test1.txt", out)
        self.assertEqual(len(out), 0)

    def test_grep_stdin(self):
        pass

    def test_grep_file_not_found(self):
        self.assertRaises(FileNotFoundError, eval, "grep he res/file.txt", deque())

    def test_grep_zero_args_invalid(self):
        self.assertRaises(ValueError, eval, "grep", deque())

    def test_grep_one_arg_invalid(self):
        self.assertRaises(ValueError, eval, "grep arg0", deque())

    def test_head(self):
        out = deque()
        eval("head res/dir1/test3.txt", out)
        self.assertEqual(list(out), [str(i) + "\n" for i in range(9)])

    def test_head_num_lines(self):
        out = deque()
        eval("head -n 5 res/dir1/test3.txt", out)
        self.assertEqual(list(out), [str(i) + "\n" for i in range(5)])

    def test_head_stdin(self):
        pass

    def test_head_stdin_num_lines(self):
        pass

    def test_head_empty_file(self):
        out = deque()
        eval("head res/dir1/empty_file.txt", out)
        self.assertEqual(len(out), 0)

    def test_head_zero_lines(self):
        out = deque()
        eval("head -n 0 res/dir1/test3.txt", out)
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

    def test_tail(self):
        out = deque()
        eval("tail res/dir1/test3.txt", out)
        self.assertEqual(list(out), [str(i) + "\n" for i in range(9)])

    def test_tail_num_lines(self):
        out = deque()
        eval("tail -n 5 res/dir1/test3.txt", out)
        self.assertEqual(list(out), [str(i) + "\n" for i in range(4, 9)])

    def test_tail_stdin(self):
        pass

    def test_tail_stdin_num_lines(self):
        pass

    def test_tail_empty_file(self):
        out = deque()
        eval("tail res/dir1/empty_file.txt", out)
        self.assertEqual(len(out), 0)

    def test_tail_zero_lines(self):
        out = deque()
        eval("tail -n 0 res/dir1/test3.txt", out)
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


if __name__ == "__main__":
    unittest.main()
