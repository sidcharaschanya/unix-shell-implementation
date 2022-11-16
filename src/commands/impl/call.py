from collections import deque
from ..command import Command
from typing import Optional


class Call(Command):
    def eval(self, input_: Optional[str], out: deque) -> None:
        pass
