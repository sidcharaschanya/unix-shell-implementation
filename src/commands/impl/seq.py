from ..command import Command
from collections import deque
from typing import Optional


class Seq(Command):
    def __init__(self, left: Command, right: Command) -> None:
        self.left = left
        self.right = right

    def eval(self, input_: Optional[str], out: deque) -> None:
        self.left.eval(input_, out)
        self.right.eval(None, out)
