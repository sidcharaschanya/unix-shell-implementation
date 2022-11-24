from ..application import Application
from collections import deque
from ..exceptions.invalid_args_error import InvalidArgsError
from ..exceptions.no_stdin_error import NoStdinError
from ..exceptions.num_args_error import NumArgsError
from ..exceptions.wrong_flags_error import WrongFlagsError
from typing import Optional
import re


class Cut(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        lines, cut_bytes = Cut.__get_lines(args, input_), args[1].split(",")

        for line in lines:
            if line.endswith("\n"):
                line = line[:-1]

            cut_indexes, cut_line = Cut.__get_cut_indexes(cut_bytes, line), ""

            for cut_index in cut_indexes:
                cut_line += line[cut_index]

            out.append(cut_line + "\n")

    @staticmethod
    def __get_lines(args: list, input_: Optional[str]) -> list:
        if len(args) < 2 or len(args) > 3:
            raise NumArgsError("Cut: wrong number of command line arguments")

        if args[0] != "-b":
            raise WrongFlagsError("Cut: wrong flags")

        if len(args) == 2:
            if input_ is None:
                raise NoStdinError("Cut: stdin not provided")

            lines = input_.splitlines(True)
        else:
            with open(args[2]) as file:
                lines = file.readlines()

        return lines

    @staticmethod
    def __get_cut_indexes(cut_bytes: list, line: str) -> list:
        len_line, cut_indexes = len(line), set()

        for cut_byte in cut_bytes:
            start, end = Cut.__get_start_and_end(cut_byte, len_line)

            for cut_index in range(start, end):
                cut_indexes.add(cut_index)

        return sorted(cut_indexes)

    @staticmethod
    def __get_start_and_end(cut_byte: str, len_line: int) -> tuple:
        if re.match("^[0-9]+$", cut_byte):
            start, end = int(cut_byte), int(cut_byte)
        elif re.match("^[0-9]+-$", cut_byte):
            start, end = int(cut_byte[:-1]), len_line + 1
        elif re.match("^-[0-9]+$", cut_byte):
            start, end = 1, int(cut_byte[1:])
        elif re.match("^[0-9]+-[0-9]+$", cut_byte):
            start = int(cut_byte.split("-")[0])
            end = int(cut_byte.split("-")[1])
        else:
            raise InvalidArgsError("Cut: invalid arguments")

        if start < 1 or end < 1:
            raise InvalidArgsError("Cut: invalid arguments")

        return start - 1, min(end, len_line)
