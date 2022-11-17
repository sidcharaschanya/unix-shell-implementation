from ..application import Application
from collections import deque
from ..exceptions.num_args_error import NumArgsError
from ..exceptions.wrong_flags_error import WrongFlagsError
from typing import Optional
import glob
import os


class Find(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) < 2 or len(args) > 3:
            raise NumArgsError("Find: wrong number of command line arguments")

        path, pattern = Find.__get_path_and_pattern(args)

        relative_paths = glob.glob(
            os.path.join(path, "**", pattern),
            recursive=True
        )

        for relative_path in relative_paths:
            out.append(relative_path + "\n")

    @staticmethod
    def __get_path_and_pattern(args: list) -> tuple:
        if len(args) == 2:
            if args[0] != "-name":
                raise WrongFlagsError("Find: wrong flags")

            path, pattern = ".", args[1]
        else:
            if args[1] != "-name":
                raise WrongFlagsError("Find: wrong flags")

            path, pattern = args[0], args[2]

        return path, pattern
