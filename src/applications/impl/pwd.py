from ..application import Application
from collections import deque
from typing import Optional
import os


class Pwd(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        if len(args) > 0:
            raise ValueError("Pwd: wrong number of command line arguments")

        out.append(os.getcwd() + "\n")
