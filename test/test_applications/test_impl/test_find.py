import unittest

from applications.impl.find import Find
from collections import deque
import shutil
import os


class TestFind(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.temp_dir = "resources"
        os.makedirs(os.path.join(self.temp_dir, "dir1", "empty_dir"))
        self.paths = dict()

        self.files = {
            "test1.txt": "",
            os.path.join("dir1", "test2.txt"): ""
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_find(self):
        Find().exec(["-name", self.paths["test1.txt"]], None, self.out)
        self.assertEqual(self.out.popleft(), os.path.join(".", self.paths["test1.txt"]) + "\n")
        self.assertEqual(len(self.out), 0)

    def test_find_pattern(self):
        Find().exec(["-name", os.path.join(self.temp_dir, "dir*")], None, self.out)
        self.assertEqual(self.out.popleft(), os.path.join(".", self.temp_dir, "dir1") + "\n")
        self.assertEqual(len(self.out), 0)

    def test_find_path(self):
        Find().exec([self.temp_dir, "-name", "*.txt"], None, self.out)
        self.assertEqual(set(self.out), {
            self.paths["test1.txt"] + "\n",
            self.paths[os.path.join("dir1", "test2.txt")] + "\n"
        })

    def test_find_empty_dir(self):
        Find().exec([os.path.join(self.temp_dir, "dir1", "empty_dir"), "-name", "*"], None, self.out)
        self.assertEqual(len(self.out), 0)

    def test_find_no_matches(self):
        Find().exec([self.temp_dir, "-name", "*.py"], None, self.out)
        self.assertEqual(len(self.out), 0)

    def test_find_zero_args_invalid(self):
        with self.assertRaises(ValueError):
            Find().exec([], None, self.out)

    def test_find_two_args_invalid(self):
        with self.assertRaises(ValueError):
            Find().exec(["arg0", "arg1"], None, self.out)

    def test_find_three_args_invalid(self):
        with self.assertRaises(ValueError):
            Find().exec(["arg0", "arg1", "arg2"], None, self.out)
