import unittest

from collections import deque
from commands.impl.call import Call
from commands.impl.seq import Seq
from hypothesis import given, strategies as st


class TestSeq(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()

    @given(st.text(), st.text())
    def test_seq(self, text_left, text_right):
        Seq(
            Call("echo", [text_left], None, None),
            Call("echo", [text_right], None, None)
        ).eval(None, self.out)
        self.assertEqual(list(self.out), [
            f"{text_left}\n",
            f"{text_right}\n"
        ])
        self.out.clear()
