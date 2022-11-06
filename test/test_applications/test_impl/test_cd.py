import unittest

from applications.impl.cd import Cd
from collections import deque
import shutil
import os


class TestCd(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        os.mkdir("resources")

    def tearDown(self) -> None:
        shutil.rmtree("resources")

    def test_cd(self):
        cwd = os.getcwd()
        Cd().exec(["resources"], None, self.out)
        self.assertEqual(os.getcwd(), os.path.join(cwd, "resources"))
        os.chdir(cwd)

    def test_cd_zero_args_invalid(self):
        with self.assertRaises(ValueError):
            Cd().exec([], None, self.out)


if __name__ == '__main__':
    unittest.main()
