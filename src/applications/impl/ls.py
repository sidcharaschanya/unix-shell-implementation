from ..application import Application
from collections import deque
from typing import Optional
import os


class Ls(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 1:
            raise ValueError("wrong number of command line arguments")

        if len(args) == 0:
            directory_name = os.getcwd()
        else:
            directory_name = args[0]

        for file_name in os.listdir(directory_name):
            if not file_name.startswith("."):
                out.append(file_name + "\n")
