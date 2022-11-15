from ..command import Command
from collections import deque
from typing import Optional
from ..visitors.evaluator import Evaluator


class Seq(Command):
    def __init__(self, left: Command, right: Command) -> None:
        self.left = left
        self.right = right

    def eval(self, e: Evaluator, input_: Optional[str], out: deque) -> None:
        e.visit_seq(self, input_, out)
