from ..application import Application
from collections import deque
from typing import Optional


class Cut(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) < 2 or len(args) > 3:
            raise ValueError("wrong number of command line arguments")

        if args[0] != "-b":
            raise ValueError("wrong flags")

        lines, cut_bytes = Cut.get_lines(args, input_), args[1].split(",")

    @staticmethod
    def get_lines(args: list, input_: Optional[str]) -> list:
        if len(args) == 2:
            if not input_:
                raise ValueError("stdin not provided")

            lines = [i + "\n" for i in input_.split("\n")]
        else:
            with open(args[2]) as file:
                lines = file.readlines()

        return lines
