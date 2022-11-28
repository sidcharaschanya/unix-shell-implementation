import unittest

from applications.exceptions.num_args_error import NumArgsError
from applications.impl.cd import Cd
from collections import deque
import shutil
import os


class TestCd(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.temp_dir = "resources"
        os.mkdir(self.temp_dir)

    def tearDown(self) -> None:
        shutil.rmtree(self.temp_dir)

    def test_cd(self):
        cwd = os.getcwd()
        Cd().exec([self.temp_dir], None, self.out)
        self.assertEqual(os.getcwd(), os.path.join(cwd, self.temp_dir))
        os.chdir(cwd)

    def test_cd_zero_args_num_args_error(self):
        with self.assertRaises(NumArgsError):
            Cd().exec([], None, self.out)
