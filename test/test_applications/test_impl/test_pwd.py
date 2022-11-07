import unittest

from applications.impl.pwd import Pwd
from collections import deque
import os


class TestPwd(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()

    def test_pwd(self):
        Pwd().exec([], None, self.out)
        self.assertEqual(self.out.popleft(), os.getcwd() + "\n")
        self.assertEqual(len(self.out), 0)

    def test_pwd_one_arg_invalid(self):
        with self.assertRaises(ValueError):
            Pwd().exec(["arg"], None, self.out)
