import unittest

from applications.impl.echo import Echo
from collections import deque
from hypothesis import given, strategies as st


class TestEcho(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()

    @given(st.text())
    def test_echo(self, text):
        Echo().exec([text], None, self.out)
        self.assertEqual(self.out.popleft(), f"{text}\n")
        self.assertEqual(len(self.out), 0)

    def test_echo_nothing(self):
        Echo().exec([], None, self.out)
        self.assertEqual(self.out.popleft(), "\n")
        self.assertEqual(len(self.out), 0)


if __name__ == '__main__':
    unittest.main()
