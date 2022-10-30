from ..application import Application
from collections import deque
from typing import Optional


class Sort(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        reverse=False
        result = []

        if len(args) == 0 and input_ is None:
            raise ValueError("wrong number of arguments")

        if len(args) == 1 and args[0] == "-r" and input_ is None:
            raise ValueError("wrong number of arguments")

        if input_ is not None:
            if len(args)==1 and args[0]!="-r":
                raise ValueError("wrong flag provided")

            if len(args) == 1 and args[0] == "-r":
                args.pop(0)
                reverse=True

            lines=[i + "\n" for i in input_.split("\n")]
            result=self.sort_file_contents(lines,reverse)

        else:
            filename=""
            if len(args)==2 and args[0]!="-r":
                raise ValueError("wrong flag provided")

            elif args[0] == "-r":
                filename = args[1]
                reverse=True
                args.pop(0)
                args.pop(0)

            else:
                filename = args[0]
                args.pop(0)

            with open(filename) as f:
                result=self.sort_file_contents(f.readlines(),reverse)


        args.extend(result)

        for arg in args:
            out.append(arg)

    def sort_file_contents(self, lines, reversed=False):
        file_contents = []
        for line in lines:
            file_contents.append(line)

        file_contents.sort(reverse=reversed)
        return file_contents
