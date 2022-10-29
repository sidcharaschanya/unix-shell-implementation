from ..application import Application
from collections import deque
from typing import Optional


class Echo(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        out.append(" ".join(args) + "\n")
