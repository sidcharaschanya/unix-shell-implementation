from ..application import Application
from ..application_utility import is_flag_and_lines
from collections import deque
from typing import Optional


class Uniq(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        ignore_case, lines = is_flag_and_lines(args, input_, "Uniq", "-i")
        previous_line = ""

        for line in lines:
            if ignore_case:
                if line.casefold() != previous_line.casefold():
                    out.append(line)
            elif line != previous_line:
                out.append(line)

            previous_line = line
