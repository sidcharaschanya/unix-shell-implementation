from ..application import Application
from collections import deque
from typing import Optional


class UnsafeDecorator(Application):
    def __init__(self, app: Application) -> None:
        self.__app = app

    def exec(self, args: list, input_: Optional[list], out: deque) -> None:
        try:
            self.__app.exec(args, input_, out)
        except Exception as exception:
            out.append(f"{exception}\n")
