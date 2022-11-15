from ..command import Command
from collections import deque
from typing import Optional


class Pipe(Command):
    def __init__(self, left: Command, right: Command) -> None:
        self.left = left
        self.right = right

    def eval(self, evaluator, input_: Optional[str], out: deque) -> None:
        evaluator.visit_pipe(self, input_, out)
