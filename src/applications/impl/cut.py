from ..application import Application
from collections import deque
from typing import Optional


class Cut(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) < 2 or len(args) > 3:
            raise ValueError("wrong number of command line arguments")

        if args[0] != "-b":
            raise ValueError("wrong flags")

        cut_bytes_string, lines = Cut.get_cut_bytes_string_and_lines(args, input_)

    @staticmethod
    def get_cut_bytes_string_and_lines(args: list, input_: Optional[str]) -> tuple:
        if len(args) == 2:
            if not input_:
                raise ValueError("stdin not provided")

            cut_bytes_string, lines = args[1], [i + "\n" for i in input_.split("\n")]
        else:
            with open(args[2]) as file:
                cut_bytes_string, lines = args[1], file.readlines()

        return cut_bytes_string, lines
