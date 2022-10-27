from .application import Application
from collections import deque
from typing import Optional


class Cat(Application):
    def exec(self, args: list, input_: Optional[list], out: deque) -> None:
        if len(args) == 0:
            if not input_ or len(input_) == 0:
                raise ValueError("stdin not provided")

            args.extend(input_)

        for arg in args:
            with open(arg) as file:
                out.append(file.read())
