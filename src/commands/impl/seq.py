from ..command import Command
from collections import deque
from typing import Optional


class Seq(Command):
    def __init__(self, left: Command, right: Command) -> None:
        self.left = left
        self.right = right

    def accept(self, command_visitor) -> None:
        command_visitor.visit_seq(self)

    def eval(self, input_: Optional[str], out: deque) -> None:
        pass
