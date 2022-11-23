from ..application import Application
from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class UnsafeDecorator(Application):
    application: Application

    def exec(self, args: list, input_: Optional[list], out: deque) -> None:
        try:
            self.application.exec(args, input_, out)
        except Exception as exception:
            out.append(f"{exception}\n")
