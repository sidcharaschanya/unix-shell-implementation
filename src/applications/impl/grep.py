from ..application import Application
from collections import deque
from typing import Optional
import re


class Grep(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) < 1:
            raise ValueError("wrong number of command line arguments")

        if len(args) == 1:
            if not input_:
                raise ValueError("stdin not provided")

            pattern = args[0]
            lines = [i + "\n" for i in input_.split("\n")]

            for line in lines:
                if re.match(pattern, line):
                    out.append(line)

        else:
            pattern = args[0]
            file_names = args[1:]

            for file_name in file_names:
                with open(file_name) as file:
                    lines = file.readlines()

                    for line in lines:
                        if re.match(pattern, line):
                            if len(file_names) > 1:
                                out.append(f"{file_name}:{line}")
                            else:
                                out.append(line)
