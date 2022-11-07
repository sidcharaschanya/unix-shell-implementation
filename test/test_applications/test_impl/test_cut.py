import unittest

from applications.impl.cut import Cut
from collections import deque
from hypothesis import given, strategies as st
import shutil
import os


class TestCut(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.temp_dir = "resources"
        os.mkdir(self.temp_dir)
        self.paths = dict()

        self.files = {
            "test1.txt": "hello world\naaa\nbbb ccc",
            "empty_file.txt": ""
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_cut(self):
        Cut().exec(["-b", "1,2,3", self.paths["test1.txt"]], None, self.out)
        self.assertEqual(list(self.out), ["hel\n", "aaa\n", "bbb\n"])

    def test_cut_interval(self):
        Cut().exec(["-b", "1-3,5-7", self.paths["test1.txt"]], None, self.out)
        # noinspection SpellCheckingInspection
        self.assertEqual(list(self.out), ["helo w\n", "aaa\n", "bbbccc\n"])

    def test_cut_start_end(self):
        Cut().exec(["-b", "-3,6-", self.paths["test1.txt"]], None, self.out)
        # noinspection SpellCheckingInspection
        self.assertEqual(list(self.out), ["hel world\n", "aaa\n", "bbbcc\n"])

    def test_cut_overlap(self):
        Cut().exec(["-b", "2-,3-", self.paths["test1.txt"]], None, self.out)
        # noinspection SpellCheckingInspection
        self.assertEqual(list(self.out), ["ello world\n", "aa\n", "bb ccc\n"])

    def test_cut_stdin(self):
        Cut().exec(["-b", "1,2,3"], self.files["test1.txt"], self.out)
        self.assertEqual(list(self.out), ["hel\n", "aaa\n", "bbb\n"])

    @given(st.integers(min_value=1))
    def test_cut_union(self, cut_byte):
        Cut().exec([
            "-b", f"-{cut_byte},{cut_byte}-", self.paths["test1.txt"]
        ], None, self.out)
        self.assertEqual(list(self.out), [
            i + "\n" for i in self.files["test1.txt"].split("\n")
        ])
        self.out.clear()

    @given(st.integers(min_value=1))
    def test_cut_empty_file(self, cut_byte):
        Cut().exec([
            "-b", str(cut_byte), self.paths["empty_file.txt"]
        ], None, self.out)
        self.assertEqual(len(self.out), 0)

    def test_cut_zero_args_invalid(self):
        with self.assertRaises(ValueError):
            Cut().exec([], None, self.out)

    def test_cut_two_args_wrong_flags(self):
        with self.assertRaises(ValueError):
            Cut().exec(["arg0", "arg1"], None, self.out)

    def test_cut_two_args_no_stdin(self):
        with self.assertRaises(ValueError):
            Cut().exec(["-b", "arg1"], None, self.out)

    def test_cut_two_args_wrong_format(self):
        with self.assertRaises(ValueError):
            Cut().exec(["-b", "-2-"], self.files["test1.txt"], self.out)

    def test_cut_two_args_zero_cut_byte(self):
        with self.assertRaises(ValueError):
            Cut().exec(["-b", "0"], self.files["test1.txt"], self.out)

    def test_cut_three_args_wrong_flags(self):
        with self.assertRaises(ValueError):
            Cut().exec(["arg0", "arg1", "arg2"], None, self.out)

    def test_cut_three_args_wrong_format(self):
        with self.assertRaises(ValueError):
            Cut().exec(["-b", "-2-", self.paths["test1.txt"]], None, self.out)

    def test_cut_three_args_zero_cut_byte(self):
        with self.assertRaises(ValueError):
            Cut().exec(["-b", "0", self.paths["test1.txt"]], None, self.out)
