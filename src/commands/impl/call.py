from applications.application_factory import ApplicationFactory
from collections import deque
from ..command import Command
from typing import Optional


class Call(Command):
    def __init__(self, app, args, in_file_name, out_file_name) -> None:
        self.app: str = app
        self.args: list = args
        self.in_file_name: Optional[str] = in_file_name
        self.out_file_name: Optional[str] = out_file_name

    def __eq__(self, other) -> bool:
        return all([
            self.__class__ == other.__class__,
            self.app == other.app,
            self.args == other.args,
            self.in_file_name == other.in_file_name,
            self.out_file_name == other.out_file_name
        ])

    def eval(self, input_: Optional[str], out: deque) -> None:
        new_in, new_out = input_, out

        if self.in_file_name is not None:
            with open(self.in_file_name) as in_file:
                new_in = "".join(in_file.readlines())

        if self.out_file_name is not None:
            new_out = deque()

        ApplicationFactory.by_name(self.app).exec(self.args, new_in, new_out)

        if self.out_file_name is not None:
            with open(self.out_file_name, "w") as out_file:
                out_file.write("".join(new_out))
