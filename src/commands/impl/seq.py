from collections import deque
from ..command import Command
from typing import Optional


class Seq(Command):
    def __init__(self, left: Command, right: Command) -> None:
        self.__left = left
        self.__right = right

    def eval(self, input_: Optional[str], out: deque) -> None:
        self.__left.eval(input_, out)
        self.__right.eval(None, out)
