from .call import Call
from collections import deque
from ..command import Command
from typing import Optional


class Pipe(Command):
    def __init__(self, left: Command, right: Call) -> None:
        self.left = left
        self.right = right

    def eval(self, input_: Optional[str], out: deque) -> None:
        temp_out = deque()
        self.left.eval(input_, temp_out)
        self.right.eval("".join(temp_out), out)
