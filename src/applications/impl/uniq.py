from ..application import Application
from collections import deque
from typing import Optional


class Uniq(Application):
    def exec(self, args: list, input_: Optional[str], out: deque) -> None:
        ignore_case = False
        result=[]

        if len(args) == 0 and input_ is None:
            raise ValueError("wrong number of arguments")

        if len(args) == 1 and args[0] == "-i" and input_ is None:
            raise ValueError("wrong number of arguments")

        if input_ is not None:
            if len(args)==1 and args[0]!="-i":
                raise ValueError("wrong flag provided")

            if len(args)==1 and args[0]=='-i':
                ignore_case=True
                args.pop(0)

            result=[i + "\n" for i in input_.split("\n")]

        else:
            filename=""
            if len(args) == 2 and args[0]!="-i":
                raise ValueError("wrong flag provided")

            if len(args) == 2 and args[0] == "-i":
                filename = args[1]
                ignore_case = True
                args.pop(0)
                args.pop(0)

            else:
                filename=args[0]
                args.pop(0)

            with open(filename) as f:
                result = self.remove_duplicate_filecontents(f.readlines(), ignore_case)

        args.extend(result)

        for arg in args:
            out.append(arg)

    def remove_duplicate_filecontents(self, lines, ignore_case=False):
        prev = ""
        result = []
        for line in lines:
            if ignore_case:
                if not prev.casefold() == line.casefold():
                    result.append(line)
            else:
                if not prev == line:
                    result.append(line)
            prev = line

        return result
