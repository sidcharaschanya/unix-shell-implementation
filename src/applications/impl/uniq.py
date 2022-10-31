from ..application import Application
from collections import deque
from typing import Optional


class Uniq(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 2:
            raise ValueError("wrong number of arguments")

        ignore_case, lines = Uniq.get_ignore_case_and_lines(args, input_)
        previous_line = ""

        for line in lines:
            if ignore_case:
                if line.casefold() != previous_line.casefold():
                    out.append(line)
            elif line != previous_line:
                out.append(line)

            previous_line = line

    @staticmethod
    def get_ignore_case_and_lines(args: list, input_: Optional[str]) -> tuple:
        if len(args) == 0:
            if not input_:
                raise ValueError("stdin not provided")

            ignore_case, lines = False, [i + "\n" for i in input_.split("\n")]
        elif len(args) == 1:
            if args[0] != "-i":
                with open(args[0]) as file:
                    ignore_case, lines = False, file.readlines()
            else:
                if not input_:
                    raise ValueError("stdin not provided")

                ignore_case, lines = True, [i + "\n" for i in input_.split("\n")]
        else:
            if args[0] != "-i":
                raise ValueError("wrong flags")

            with open(args[1]) as file:
                ignore_case, lines = True, file.readlines()

        return ignore_case, lines
