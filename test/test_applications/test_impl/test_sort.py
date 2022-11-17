import unittest

from applications.exceptions.no_stdin_error import NoStdinError
from applications.exceptions.num_args_error import NumArgsError
from applications.exceptions.wrong_flags_error import WrongFlagsError
from applications.impl.sort import Sort
from collections import deque
import shutil
import os


class TestSort(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.temp_dir = "resources"
        os.mkdir(self.temp_dir)
        self.paths = dict()

        self.files = {
            "test1.txt": "hello world\naaa",
            "empty_file.txt": ""
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_sort(self):
        Sort().exec([self.paths["test1.txt"]], None, self.out)
        self.assertEqual(list(self.out), ["aaa\n", "hello world\n"])

    def test_sort_reverse(self):
        Sort().exec(["-r", self.paths["test1.txt"]], None, self.out)
        self.assertEqual(list(self.out), ["hello world\n", "aaa\n"])

    def test_sort_stdin(self):
        Sort().exec([], self.files["test1.txt"], self.out)
        self.assertEqual(list(self.out), ["aaa\n", "hello world\n"])

    def test_sort_stdin_reverse(self):
        Sort().exec(["-r"], self.files["test1.txt"], self.out)
        self.assertEqual(list(self.out), ["hello world\n", "aaa\n"])

    def test_sort_empty_file(self):
        Sort().exec([self.paths["empty_file.txt"]], None, self.out)
        self.assertEqual(len(self.out), 0)

    def test_sort_empty_file_reverse(self):
        Sort().exec(["-r", self.paths["empty_file.txt"]], None, self.out)
        self.assertEqual(len(self.out), 0)

    def test_sort_zero_args_no_stdin_error(self):
        with self.assertRaises(NoStdinError):
            Sort().exec([], None, self.out)

    def test_sort_one_arg_no_stdin_error(self):
        with self.assertRaises(NoStdinError):
            Sort().exec(["-r"], None, self.out)

    def test_sort_one_arg_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            Sort().exec([
                os.path.join(self.temp_dir, "file.txt")
            ], None, self.out)

    def test_sort_two_args_wrong_flags_error(self):
        with self.assertRaises(WrongFlagsError):
            Sort().exec(["arg0", "arg1"], None, self.out)

    def test_sort_two_args_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            Sort().exec([
                "-r", os.path.join(self.temp_dir, "file.txt")
            ], None, self.out)

    def test_sort_three_args_num_args_error(self):
        with self.assertRaises(NumArgsError):
            Sort().exec(["arg0", "arg1", "arg2"], None, self.out)
