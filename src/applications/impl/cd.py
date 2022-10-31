from ..application import Application
from collections import deque
from typing import Optional
import os


class Cd(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) == 0 or len(args) > 1:
            raise ValueError("wrong number of command line arguments")

        os.chdir(args[0])
