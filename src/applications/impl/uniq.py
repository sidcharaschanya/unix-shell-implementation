from ..application import Application
from collections import deque
from typing import Optional


class Uniq(Application):
    def exec(self, args: list, input_: Optional[list], out: deque) -> None:
        filename=""
        ignore_case=False
        if len(args)==0 and input_ is None:
            raise ValueError("wrong number of arguments")

        if len(args)==1 and args[0]=="-i" and input_ is None:
            raise ValueError("wrong number of arguments")

        if len(args)==0:
            filename=input_[0]

        elif len(args) == 1 and args[0] == "-i":
            filename = input_[0]
            ignore_case=True
            args.pop(0)

        elif len(args) ==2 and args[0]=="-i":
                filename=args[1]
                ignore_case=True
                args.pop(0)
                args.pop(0)

        else:
            filename=args[0]
            args.pop(0)

        result = self.remove_duplicate_filecontents(filename, ignore_case)
        args.extend(result)

        for arg in args:
            out.append(arg)


    def remove_duplicate_filecontents(self,filename,ignore_case=False):
        prev=""
        result=[]
        with open(filename) as f:
            lines=f.readlines()
            for line in lines:
                if ignore_case:
                    if not prev.casefold() == line.casefold():
                        result.append(line)
                else:
                    if not prev == line:
                        result.append(line)
                prev=line

        return result