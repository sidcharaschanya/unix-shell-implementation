from ..application import Application
from collections import deque
from typing import Optional
import glob
import os


class Find(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) < 2 or len(args) > 3:
            raise ValueError("wrong number of command line arguments")

        path, pattern = Find.get_path_and_pattern(args)

        for relative_path in glob.glob(os.path.join(path, "**", pattern), recursive=True):
            out.append(relative_path + "\n")

    @staticmethod
    def get_path_and_pattern(args: list) -> tuple:
        if len(args) == 2:
            if args[0] != "-name":
                raise ValueError("wrong flags")

            path, pattern = ".", args[1]
        else:
            if args[1] != "-name":
                raise ValueError("wrong flags")

            path, pattern = args[0], args[2]

        return path, pattern
