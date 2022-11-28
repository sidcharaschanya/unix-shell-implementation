from applications.application_factory import ApplicationFactory
from collections import deque
from ..command import Command
from dataclasses import dataclass
from typing import Optional


@dataclass
class Call(Command):
    app: str
    args: list
    in_file_name: Optional[str]
    out_file_name: Optional[str]

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
