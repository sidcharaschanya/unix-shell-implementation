from application import Application
from collections import deque
from typing import Optional


class Cat(Application):
    def exec(self, args: list, input_: Optional[deque], out: deque) -> None:
        if len(args) == 0:
            if not input_:
                raise ValueError("stdin not provided")

            args.extend(input_)

        for arg in args:
            with open(arg) as file:
                out.append(file.read())
