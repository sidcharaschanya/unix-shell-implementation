from ..command import Command
from collections import deque
from typing import Optional


class Call(Command):
    def eval(self, input_: Optional[str], out: deque) -> None:
        pass
