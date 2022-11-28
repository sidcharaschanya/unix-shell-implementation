from .exceptions.invalid_args_error import InvalidArgsError
from .exceptions.no_stdin_error import NoStdinError
from .exceptions.num_args_error import NumArgsError
from .exceptions.wrong_flags_error import WrongFlagsError
from typing import Optional as Opt


def display_length_and_lines(args: list, in_: Opt[str], app: str) -> tuple:
    if len(args) > 3:
        raise NumArgsError(f"{app}: wrong number of command line arguments")

    if len(args) == 0:
        if in_ is None:
            raise NoStdinError(f"{app}: stdin not provided")

        num_lines, lines = 10, in_.splitlines(True)
    elif len(args) == 1:
        with open(args[0]) as file:
            num_lines, lines = 10, file.readlines()
    elif len(args) == 2:
        if args[0] != "-n":
            raise WrongFlagsError(f"{app}: wrong flags")

        if in_ is None:
            raise NoStdinError(f"{app}: stdin not provided")

        num_lines, lines = int(args[1]), in_.splitlines(True)
    else:
        if args[0] != "-n":
            raise WrongFlagsError(f"{app}: wrong flags")

        with open(args[2]) as file:
            num_lines, lines = int(args[1]), file.readlines()

    if num_lines < 0:
        raise InvalidArgsError(f"{app}: invalid arguments")

    return min(len(lines), num_lines), lines


def is_flag_and_lines(args: list, in_: Opt[str], app: str, flag: str) -> tuple:
    if len(args) > 2:
        raise NumArgsError(f"{app}: wrong number of arguments")

    if len(args) == 0:
        if in_ is None:
            raise NoStdinError(f"{app}: stdin not provided")

        is_flag, lines = False, in_.splitlines(True)
    elif len(args) == 1:
        if args[0] != flag:
            with open(args[0]) as file:
                is_flag, lines = False, file.readlines()
        else:
            if in_ is None:
                raise NoStdinError(f"{app}: stdin not provided")

            is_flag, lines = True, in_.splitlines(True)
    else:
        if args[0] != flag:
            raise WrongFlagsError(f"{app}: wrong flags")

        with open(args[1]) as file:
            is_flag, lines = True, file.readlines()

    return is_flag, lines
