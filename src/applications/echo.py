from application import Application
from collections import deque
from typing import Optional


class Echo(Application):
    def exec(self, args: list, input_: Optional[deque], out: deque) -> None:
        pass
