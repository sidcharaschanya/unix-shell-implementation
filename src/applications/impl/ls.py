from ..application import Application
from collections import deque
from ..exceptions.num_args_error import NumArgsError
from typing import Optional
import os


class Ls(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        directory_name = Ls.__get_directory_name(args)

        for file_name in os.listdir(directory_name):
            if not file_name.startswith("."):
                out.append(file_name + "\t")

        out.append("\n")

    @staticmethod
    def __get_directory_name(args: list) -> str:
        if len(args) > 1:
            raise NumArgsError("Ls: wrong number of command line arguments")

        if len(args) == 0:
            directory_name = os.getcwd()
        else:
            directory_name = args[0]

        return directory_name
