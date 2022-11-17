from ..application import Application
from collections import deque
from ..exceptions.num_args_error import NumArgsError
from typing import Optional
import os


class Pwd(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 0:
            raise NumArgsError("Pwd: wrong number of command line arguments")

        out.append(os.getcwd() + "\n")
