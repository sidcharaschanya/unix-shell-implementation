from ..application import Application
from collections import deque
from typing import Optional


class Sort(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 2:
            raise ValueError("wrong number of arguments")

        reverse, lines = Sort.__get_reverse_and_lines(args, input_)

        for line in sorted(lines, reverse=reverse):
            out.append(line)

    @staticmethod
    def __get_reverse_and_lines(args: list, input_: Optional[str]) -> tuple:
        if len(args) == 0:
            if not input_:
                raise ValueError("stdin not provided")

            reverse, lines = False, [i + "\n" for i in input_.split("\n")]
        elif len(args) == 1:
            if args[0] != "-r":
                with open(args[0]) as file:
                    reverse, lines = False, file.readlines()
            else:
                if not input_:
                    raise ValueError("stdin not provided")

                reverse, lines = True, [i + "\n" for i in input_.split("\n")]
        else:
            if args[0] != "-r":
                raise ValueError("wrong flags")

            with open(args[1]) as file:
                reverse, lines = True, file.readlines()

        return reverse, lines
