from ..application import Application
from collections import deque
from ..exceptions.invalid_args_error import InvalidArgsError
from ..exceptions.no_stdin_error import NoStdinError
from ..exceptions.num_args_error import NumArgsError
from ..exceptions.wrong_flags_error import WrongFlagsError
from typing import Optional


class Tail(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 3:
            raise NumArgsError("Tail: wrong number of command line arguments")

        num_lines, lines = Tail.__get_num_lines_and_lines(args, input_)
        display_length = min(len(lines), num_lines)

        for i in range(0, display_length):
            out.append(lines[len(lines) - display_length + i])

    @staticmethod
    def __get_num_lines_and_lines(args: list, input_: Optional[str]) -> tuple:
        if len(args) == 0:
            if input_ is None:
                raise NoStdinError("Tail: stdin not provided")

            num_lines, lines = 10, input_.splitlines(True)
        elif len(args) == 1:
            with open(args[0]) as file:
                num_lines, lines = 10, file.readlines()
        elif len(args) == 2:
            if args[0] != "-n":
                raise WrongFlagsError("Tail: wrong flags")

            if input_ is None:
                raise NoStdinError("Tail: stdin not provided")

            num_lines, lines = int(args[1]), input_.splitlines(True)
        else:
            if args[0] != "-n":
                raise WrongFlagsError("Tail: wrong flags")

            with open(args[2]) as file:
                num_lines, lines = int(args[1]), file.readlines()

        if num_lines < 0:
            raise InvalidArgsError("Tail: invalid arguments")

        return num_lines, lines
