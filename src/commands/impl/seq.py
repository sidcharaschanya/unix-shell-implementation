from collections import deque
from ..command import Command
from dataclasses import dataclass
from typing import Optional


@dataclass
class Seq(Command):
    left: Command
    right: Command

    def eval(self, input_: Optional[str], out: deque) -> None:
        self.left.eval(input_, out)
        self.right.eval(None, out)
