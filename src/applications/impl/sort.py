from ..application import Application
from collections import deque
from ..exceptions.no_stdin_error import NoStdinError
from ..exceptions.num_args_error import NumArgsError
from ..exceptions.wrong_flags_error import WrongFlagsError
from typing import Optional


class Sort(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 2:
            raise NumArgsError("Sort: wrong number of arguments")

        reverse, lines = Sort.__get_reverse_and_lines(args, input_)

        for line in sorted(lines, reverse=reverse):
            out.append(line if line.endswith("\n") else line + "\n")

    @staticmethod
    def __get_reverse_and_lines(args: list, input_: Optional[str]) -> tuple:
        if len(args) == 0:
            if input_ is None:
                raise NoStdinError("Sort: stdin not provided")

            reverse, lines = False, input_.splitlines(True)
        elif len(args) == 1:
            if args[0] != "-r":
                with open(args[0]) as file:
                    reverse, lines = False, file.readlines()
            else:
                if input_ is None:
                    raise NoStdinError("Sort: stdin not provided")

                reverse, lines = True, input_.splitlines(True)
        else:
            if args[0] != "-r":
                raise WrongFlagsError("Sort: wrong flags")

            with open(args[1]) as file:
                reverse, lines = True, file.readlines()

        return reverse, lines
