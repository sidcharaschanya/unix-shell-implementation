import unittest

from applications.impl.grep import Grep
from collections import deque
from hypothesis import given, strategies as st
import shutil
import os


class TestGrep(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.temp_dir = "resources"
        os.mkdir(self.temp_dir)
        self.paths = dict()

        self.files = {
            "test1.txt": "hello\n",
            "test2.txt": "hehehehe\nhellohello\n",
            "empty_file.txt": ""
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_grep(self):
        Grep().exec([
            "he", os.path.join(self.temp_dir, "test1.txt")
        ], None, self.out)
        self.assertEqual(self.out.popleft(), "hello\n")
        self.assertEqual(len(self.out), 0)

    def test_grep_multiple_files(self):
        Grep().exec([
            "he",
            os.path.join(self.temp_dir, "test1.txt"),
            os.path.join(self.temp_dir, "test2.txt")
        ], None, self.out)
        self.assertEqual(list(self.out), [
            "resources/test1.txt:hello\n",
            "resources/test2.txt:hehehehe\n",
            "resources/test2.txt:hellohello\n",
        ])

    @given(st.text())
    def test_grep_empty_file(self, pattern):
        Grep().exec([
            pattern, os.path.join(self.temp_dir, "empty_file.txt")
        ], None, self.out)
        self.assertEqual(len(self.out), 0)

    def test_grep_no_matches(self):
        Grep().exec([
            "aa", os.path.join(self.temp_dir, "test1.txt")
        ], None, self.out)
        self.assertEqual(len(self.out), 0)

    def test_grep_stdin(self):
        Grep().exec(["he"], self.files["test2.txt"], self.out)
        self.assertEqual(list(self.out), ["hehehehe\n", "hellohello\n"])

    def test_grep_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            Grep().exec([
                "he", os.path.join(self.temp_dir, "file.txt")
            ], None, self.out)

    def test_grep_zero_args_invalid(self):
        with self.assertRaises(ValueError):
            Grep().exec([], None, self.out)

    def test_grep_one_arg_invalid(self):
        with self.assertRaises(ValueError):
            Grep().exec(["arg0"], None, self.out)
