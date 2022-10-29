from ..application import Application
from collections import deque
from typing import Optional
import re

# grep 'A..' pattern left for quoting
class Grep(Application):
    def exec(self, args: list, input_: Optional[list], out: deque) -> None:
        if len(args)<1:
            raise ValueError("wrong number of command line arguments")

        if len(args)==1 and input_ is None:
            raise ValueError("wrong number of command line arguments")

        elif len(args)==1 and input_ is not None:
            args.extend(input_)
            pattern=args[0]
            inputData=args[1:]

            for item in inputData:
                if re.match(pattern,item):
                    out.append(item)

        else:
            pattern = args[0]
            files = args[1:]

            for file in files:
                with open(file) as f:
                    lines = f.readlines()
                    for line in lines:
                        if re.match(pattern, line):
                            if len(files) > 1:
                                out.append(f"{file}:{line}")
                            else:
                                out.append(line)






