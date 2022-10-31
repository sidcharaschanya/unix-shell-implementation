from ..application import Application
from collections import deque
from typing import Optional
import re


class Cut(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) < 2 or len(args) > 3:
            raise ValueError("wrong number of command line arguments")

        if args[0] != "-b":
            raise ValueError("wrong flags")

        lines, cut_byte_strings = Cut.get_lines(args, input_), args[1].split(",")

        for line in lines:
            if line.endswith("\n"):
                line = line[:-1]

            cut_line = ""

            for cut_byte in Cut.get_cut_bytes(cut_byte_strings, line):
                cut_line += line[cut_byte]

            out.append(cut_line + "\n")

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

    @staticmethod
    def get_cut_bytes(cut_byte_strings: list, line: str) -> list:
        len_line, cut_bytes = len(line), set()

        for cut_byte_string in cut_byte_strings:
            start, end = Cut.get_start_and_end(cut_byte_string, len_line)

            for cut_byte in range(start, end):
                cut_bytes.add(cut_byte)

        return sorted(cut_bytes)

    @staticmethod
    def get_start_and_end(cut_byte_string: str, len_line: int) -> tuple:
        if re.match("^[0-9]+$", cut_byte_string):
            start, end = int(cut_byte_string), int(cut_byte_string)
        elif re.match("^[0-9]+-$", cut_byte_string):
            start, end = int(cut_byte_string[:-1]), len_line + 1
        elif re.match("^-[0-9]+$", cut_byte_string):
            start, end = 1, int(cut_byte_string[1:])
        elif re.match("^[0-9]+-[0-9]+$", cut_byte_string):
            start, end = int(cut_byte_string.split("-")[0]), int(cut_byte_string.split("-")[1])
        else:
            raise ValueError("invalid arguments")

        if start < 1 or end < 1:
            raise ValueError("invalid arguments")

        return start - 1, min(end, len_line)
