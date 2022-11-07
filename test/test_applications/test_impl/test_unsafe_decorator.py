import unittest

from applications.impl.ls import Ls
from applications.impl.unsafe_decorator import UnsafeDecorator
from collections import deque
from hypothesis import given, strategies as st
import os


class TestUnsafeDecorator(unittest.TestCase):
    @given(st.text(min_size=1))
    def test_unsafe_decorator_ls(self, directory_name):
        out = deque()
        UnsafeDecorator(Ls()).exec([
            os.path.join("resources", directory_name)
        ], None, deque())
        self.assertEqual(len(out), 0)
