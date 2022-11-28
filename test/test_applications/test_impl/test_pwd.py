import unittest

from applications.exceptions.num_args_error import NumArgsError
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

    def test_pwd_one_arg_num_args_error(self):
        with self.assertRaises(NumArgsError):
            Pwd().exec(["arg0"], None, self.out)
