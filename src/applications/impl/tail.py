from ..application import Application
from collections import deque
from typing import Optional


class Tail(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 3:
            raise ValueError("wrong number of command line arguments")

        num_lines, lines = Tail.get_num_lines_and_lines(args, input_)
        display_length = min(len(lines), num_lines)

        for i in range(0, display_length):
            out.append(lines[len(lines) - display_length + i])

    @staticmethod
    def get_num_lines_and_lines(args: list, input_: Optional[str]) -> tuple:
        if len(args) == 0:
            if not input_:
                raise ValueError("stdin not provided")

            num_lines, lines = 10, [i + "\n" for i in input_.split("\n")]
        elif len(args) == 1:
            with open(args[0]) as file:
                num_lines, lines = 10, file.readlines()
        elif len(args) == 2:
            if args[0] != "-n":
                raise ValueError("wrong flags")

            if not input_:
                raise ValueError("stdin not provided")

            num_lines, lines = int(args[1]), [i + "\n" for i in input_.split("\n")]
        else:
            if args[0] != "-n":
                raise ValueError("wrong flags")

            with open(args[2]) as file:
                num_lines, lines = int(args[1]), file.readlines()

        return num_lines, lines