from ..application import Application
from collections import deque
from typing import Optional


class Sort(Application):
    def exec(self, args: list, input_: Optional[list], out: deque) -> None:
        if len(args)==0 and input_ is None:
            raise ValueError("wrong number of arguments")

        if len(args)==1 and args[0]=="-r" and input_ is None:
            raise ValueError("wrong number of arguments")

        if input_ is not None:
            if len(args)==1 and args[0]=="-r":
                args.pop(0)
                args.extend(input_)
                args.sort(reverse=True)

            else:
                args.extend(input_)
                args.sort()

        else:
            if args[0]=="-r":
                filename=args[1]

                result=self.sort_file_contents(filename,True)
                args.pop(0)
                args.pop(0)
                args.extend(result)
            else:
                filename=args[0]
                args.pop(0)
                result=self.sort_file_contents(filename)
                args.extend(result)

        for arg in args:
            out.append(arg)


    def sort_file_contents(self,filename,reversed=False):
        file_content=[]
        with open(filename) as f:
            lines=f.readlines()
            for line in lines:
                file_content.append(line)

        file_content.sort(reverse=reversed)
        return file_content


