from collections import deque
from ..command import Command
from typing import Optional


class Seq(Command):
    def __init__(self, left: Command, right: Command) -> None:
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        return all([
            self.__class__ == other.__class__,
            self.left == other.left,
            self.right == other.right
        ])

    def eval(self, input_: Optional[str], out: deque) -> None:
        self.left.eval(input_, out)
        self.right.eval(None, out)
