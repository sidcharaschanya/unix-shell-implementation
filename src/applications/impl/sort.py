from ..application import Application
from ..application_utility import is_flag_and_lines
from collections import deque
from typing import Optional


class Sort(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        reverse, lines = is_flag_and_lines(args, input_, "Sort", "-r")

        for line in sorted(lines, reverse=reverse):
            out.append(line if line.endswith("\n") else line + "\n")
