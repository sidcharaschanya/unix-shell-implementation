import unittest

from applications.impl.tail import Tail
from collections import deque
from hypothesis import given, strategies as st
import shutil
import os


class TestTail(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.temp_dir = "resources"
        os.mkdir(self.temp_dir)
        self.paths = dict()

        self.files = {
            "test1.txt": "0\n1\n2\n3\n4\n5\n6\n7\n8\n",
            "empty_file.txt": ""
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_tail(self):
        Tail().exec([self.paths["test1.txt"]], None, self.out)
        self.assertEqual(list(self.out), [str(i) + "\n" for i in range(9)])

    @given(st.integers(min_value=0, max_value=9))
    def test_tail_num_lines(self, num_lines):
        Tail().exec(["-n", str(num_lines), self.paths["test1.txt"]], None, self.out)
        self.assertEqual(list(self.out), [str(i) + "\n" for i in range(9 - num_lines, 9)])
        self.out.clear()

    def test_tail_stdin(self):
        Tail().exec([], self.files["test1.txt"][:-1], self.out)
        self.assertEqual(list(self.out), [str(i) + "\n" for i in range(9)])

    @given(st.integers(min_value=0, max_value=9))
    def test_tail_stdin_num_lines(self, num_lines):
        Tail().exec(["-n", str(num_lines)], self.files["test1.txt"][:-1], self.out)
        self.assertEqual(list(self.out), [str(i) + "\n" for i in range(9 - num_lines, 9)])
        self.out.clear()

    @given(st.integers(min_value=0))
    def test_tail_empty_file(self, num_lines):
        Tail().exec(["-n", str(num_lines), self.paths["empty_file.txt"]], None, self.out)
        self.assertEqual(len(self.out), 0)

    @given(st.text())
    def test_tail_zero_lines(self, stdin):
        Tail().exec(["-n", "0"], stdin, self.out)
        self.assertEqual(len(self.out), 0)

    @given(st.integers(max_value=-1))
    def test_tail_negative_num_lines(self, num_lines):
        with self.assertRaises(ValueError):
            Tail().exec(["-n", str(num_lines), self.paths["test1.txt"]], None, self.out)

    def test_tail_zero_args_invalid(self):
        with self.assertRaises(ValueError):
            Tail().exec([], None, self.out)

    def test_tail_two_args_wrong_flags(self):
        with self.assertRaises(ValueError):
            Tail().exec(["arg0", "arg1"], None, self.out)

    def test_tail_two_args_no_stdin(self):
        with self.assertRaises(ValueError):
            Tail().exec(["-n", "arg1"], None, self.out)

    def test_tail_three_args_invalid(self):
        with self.assertRaises(ValueError):
            Tail().exec(["arg0", "arg1", "arg2"], None, self.out)

    def test_tail_four_args_invalid(self):
        with self.assertRaises(ValueError):
            Tail().exec(["arg0", "arg1", "arg2", "arg3"], None, self.out)
