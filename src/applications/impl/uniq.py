from ..application import Application
from collections import deque
from ..exceptions.no_stdin_error import NoStdinError
from ..exceptions.num_args_error import NumArgsError
from ..exceptions.wrong_flags_error import WrongFlagsError
from typing import Optional


class Uniq(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 2:
            raise NumArgsError("Uniq: wrong number of arguments")

        ignr_case, lines = Uniq.__get_ignr_case_and_lines(args, input_)
        previous_line = ""

        for line in lines:
            if line.endswith("\n"):
                line = line[:-1]

            if ignr_case:
                if line.casefold() != previous_line.casefold():
                    out.append(line + "\n")
            elif line != previous_line:
                out.append(line + "\n")

            previous_line = line

    @staticmethod
    def __get_ignr_case_and_lines(args: list, input_: Optional[str]) -> tuple:
        if len(args) == 0:
            if input_ is None:
                raise NoStdinError("Uniq: stdin not provided")

            ignr_case, lines = False, [i + "\n" for i in input_.split("\n")]
        elif len(args) == 1:
            if args[0] != "-i":
                with open(args[0]) as file:
                    ignr_case, lines = False, file.readlines()
            else:
                if input_ is None:
                    raise NoStdinError("Uniq: stdin not provided")

                ignr_case, lines = True, [i + "\n" for i in input_.split("\n")]
        else:
            if args[0] != "-i":
                raise WrongFlagsError("Uniq: wrong flags")

            with open(args[1]) as file:
                ignr_case, lines = True, file.readlines()

        return ignr_case, lines
