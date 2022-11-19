from .call import Call
from collections import deque
from ..command import Command
from typing import Optional


class Pipe(Command):
    def __init__(self, left: Command, right: Call) -> None:
        self.__left = left
        self.__right = right

    def eval(self, input_: Optional[str], out: deque) -> None:
        temp_out = deque()
        self.__left.eval(input_, temp_out)
        self.__right.eval("".join(temp_out), out)
