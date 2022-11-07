import unittest

from applications.impl.cat import Cat
from collections import deque
from hypothesis import given, strategies as st
import shutil
import os


class TestCat(unittest.TestCase):
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

    def test_cat(self):
        Cat().exec([self.paths["test1.txt"], self.paths["test2.txt"]], None, self.out)
        self.assertEqual(list(self.out), ["hello\n", "hehehehe\nhellohello\n"])

    def test_cat_empty_file(self):
        Cat().exec([self.paths["empty_file.txt"]], None, self.out)
        self.assertEqual(self.out.popleft(), "")
        self.assertEqual(len(self.out), 0)

    @given(st.text())
    def test_cat_stdin(self, stdin):
        Cat().exec([], stdin, self.out)
        self.assertEqual(self.out.popleft(), stdin)
        self.assertEqual(len(self.out), 0)

    def test_cat_zero_args_invalid(self):
        with self.assertRaises(ValueError):
            Cat().exec([], None, self.out)
