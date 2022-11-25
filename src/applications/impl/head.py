from ..application import Application
from ..application_utility import display_length_and_lines
from collections import deque
from typing import Optional


class Head(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        display_length, lines = display_length_and_lines(args, input_, "Head")

        for i in range(0, display_length):
            out.append(lines[i])
