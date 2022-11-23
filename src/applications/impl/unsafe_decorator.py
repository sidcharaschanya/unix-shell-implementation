from ..application import Application
from collections import deque
from typing import Optional


class UnsafeDecorator(Application):
    def __init__(self, application: Application) -> None:
        self.app = application

    def exec(self, args: list, input_: Optional[list], out: deque) -> None:
        try:
            self.app.exec(args, input_, out)
        except Exception as exception:
            out.append(f"{exception}\n")
