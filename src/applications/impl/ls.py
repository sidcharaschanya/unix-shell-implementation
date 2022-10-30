from ..application import Application
from collections import deque
from typing import Optional
import os


class Ls(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 1:
            raise ValueError("wrong number of command line arguments")

        if len(args) == 0:
            ls_directory = os.getcwd()
        else:
            ls_directory = args[0]

        for file_name in os.listdir(ls_directory):
            if not file_name.startswith("."):
                out.append(file_name + "\n")
