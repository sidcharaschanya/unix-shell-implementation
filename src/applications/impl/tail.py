from ..application import Application
from collections import deque
from typing import Optional


class Tail(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 3:
            raise ValueError("wrong number of command line arguments")

        if len(args) == 0:
            if not input_:
                raise ValueError("stdin not provided")

            Tail.lines(10, [i + "\n" for i in input_.split("\n")], out)
        elif len(args) == 1:
            with open(args[0]) as file:
                Tail.lines(10, file.readlines(), out)
        elif len(args) == 2:
            if args[0] != "-n":
                raise ValueError("wrong flags")

            if not input_:
                raise ValueError("stdin not provided")

            Tail.lines(int(args[1]), [i + "\n" for i in input_.split("\n")], out)
        else:
            if args[0] != "-n":
                raise ValueError("wrong flags")

            with open(args[2]) as file:
                Tail.lines(int(args[1]), file.readlines(), out)

    @staticmethod
    def lines(num_lines: int, input_lines: list, out: deque) -> None:
        display_length = min(len(input_lines), num_lines)

        for i in range(0, display_length):
            out.append(input_lines[len(input_lines) - display_length + i])
