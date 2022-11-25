import unittest

from applications.exceptions.no_stdin_error import NoStdinError
from applications.exceptions.num_args_error import NumArgsError
from applications.exceptions.wrong_flags_error import WrongFlagsError
from applications.impl.uniq import Uniq
from collections import deque
import shutil
import os


class TestUniq(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.temp_dir = "resources"
        os.mkdir(self.temp_dir)
        self.paths = dict()

        self.files = {
            "test1.txt": "aaa\naaa\nAAA\naaa\n",
            "empty_file.txt": ""
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_uniq(self):
        Uniq().exec([self.paths["test1.txt"]], None, self.out)
        self.assertEqual(list(self.out), ["aaa\n", "AAA\n", "aaa\n"])

    def test_uniq_ignore_case(self):
        Uniq().exec(["-i", self.paths["test1.txt"]], None, self.out)
        self.assertEqual(list(self.out), ["aaa\n"])

    def test_uniq_stdin(self):
        Uniq().exec([], self.files["test1.txt"], self.out)
        self.assertEqual(list(self.out), ["aaa\n", "AAA\n", "aaa\n"])

    def test_uniq_stdin_ignore_case(self):
        Uniq().exec(["-i"], self.files["test1.txt"], self.out)
        self.assertEqual(list(self.out), ["aaa\n"])

    def test_uniq_empty_file(self):
        Uniq().exec([self.paths["empty_file.txt"]], None, self.out)
        self.assertEqual(len(self.out), 0)

    def test_uniq_empty_file_ignore_case(self):
        Uniq().exec(["-i", self.paths["empty_file.txt"]], None, self.out)
        self.assertEqual(len(self.out), 0)

    def test_uniq_zero_args_no_stdin_error(self):
        with self.assertRaises(NoStdinError):
            Uniq().exec([], None, self.out)

    def test_uniq_one_arg_no_stdin_error(self):
        with self.assertRaises(NoStdinError):
            Uniq().exec(["-i"], None, self.out)

    def test_uniq_one_arg_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            Uniq().exec([
                os.path.join(self.temp_dir, "file.txt")
            ], None, self.out)

    def test_uniq_two_args_wrong_flags_error(self):
        with self.assertRaises(WrongFlagsError):
            Uniq().exec(["arg0", "arg1"], None, self.out)

    def test_uniq_two_args_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            Uniq().exec([
                "-i", os.path.join(self.temp_dir, "file.txt")
            ], None, self.out)

    def test_uniq_three_args_num_args_error(self):
        with self.assertRaises(NumArgsError):
            Uniq().exec(["arg0", "arg1", "arg2"], None, self.out)
