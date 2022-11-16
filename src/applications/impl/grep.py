from ..application import Application
from collections import deque
from typing import Optional
import re


class Grep(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) == 0:
            raise ValueError("Grep: wrong number of command line arguments")

        if len(args) == 1:
            Grep.__one_arg(args, input_, out)
        else:
            Grep.__two_or_more_args(args, out)

    @staticmethod
    def __one_arg(args: list, input_: Optional[str], out: deque) -> None:
        if input_ is None:
            raise ValueError("Grep: stdin not provided")

        pattern, lines = args[0], [i + "\n" for i in input_.split("\n")]

        for line in lines:
            if re.match(pattern, line):
                out.append(line)

    @staticmethod
    def __two_or_more_args(args: list, out: deque) -> None:
        pattern, file_names = args[0], args[1:]

        for file_name in file_names:
            with open(file_name) as file:
                lines = file.readlines()

                for line in lines:
                    if re.match(pattern, line):
                        if len(file_names) > 1:
                            out.append(f"{file_name}:{line}")
                        else:
                            out.append(line)
