from .call import Call
from collections import deque
from ..command import Command
from dataclasses import dataclass
from typing import Optional


@dataclass
class Pipe(Command):
    left: Command
    right: Call

    def eval(self, input_: Optional[str], out: deque) -> None:
        temp_out = deque()
        self.left.eval(input_, temp_out)
        self.right.eval("".join(temp_out), out)
