import unittest

from applications.impl.ls import Ls
from applications.impl.unsafe_decorator import UnsafeDecorator
from collections import deque
from hypothesis import given, strategies as st
import shutil
import os


class TestUnsafeDecorator(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        os.mkdir("resources")

    def tearDown(self) -> None:
        shutil.rmtree("resources")

    @given(st.text(min_size=1))
    def test_unsafe_decorator_ls(self, directory_name):
        UnsafeDecorator(Ls()).exec([os.path.join("resources", directory_name)], None, self.out)
        self.assertEqual(len(self.out), 0)


if __name__ == '__main__':
    unittest.main()
