import unittest

from applications.impl.ls import Ls
from collections import deque
import shutil
import os


class TestLs(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.temp_dir = "resources"
        os.makedirs(os.path.join(self.temp_dir, "empty_dir"))
        self.paths = dict()

        self.files = {
            "test1.txt": "",
            ".hidden1.txt": ""
        }

        for file_name, file_content in self.files.items():
            with open(os.path.join(self.temp_dir, file_name), "w") as file:
                file.write(file_content)
                self.paths[file_name] = file.name

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_ls(self):
        cwd = os.getcwd()
        os.chdir(self.temp_dir)
        Ls().exec([], None, self.out)
        self.assertEqual(set(self.out), {"empty_dir\t", "test1.txt\t", "\n"})
        os.chdir(cwd)

    def test_ls_path(self):
        Ls().exec([self.temp_dir], None, self.out)
        self.assertEqual(set(self.out), {"empty_dir\t", "test1.txt\t", "\n"})

    def test_ls_empty_dir(self):
        Ls().exec([os.path.join(self.temp_dir, "empty_dir")], None, self.out)
        self.assertEqual(self.out.popleft(), "\n")
        self.assertEqual(len(self.out), 0)

    def test_ls_two_args_invalid(self):
        with self.assertRaises(ValueError):
            Ls().exec(["arg0", "arg1"], None, self.out)
