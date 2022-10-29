import re
import sys
import os
from collections import deque
# from glob import glob
from applications.application_factory import ApplicationFactory


def eval(cmdline: str, out: deque) -> None:
    raw_commands = []
    for m in re.finditer("([^\"';]+|\"[^\"]*\"|'[^']*')", cmdline):
        if m.group(0):
            raw_commands.append(m.group(0))
    for command in raw_commands:
        tokens = []
        for m in re.finditer("[^\\s\"']+|\"([^\"]*)\"|'([^']*)'", command):
            if m.group(1) or m.group(2):
                quoted = m.group(0)
                tokens.append(quoted[1:-1])
            else:
                # globbing = glob(m.group(0))
                # if globbing:
                #     tokens.extend(globbing)
                # else:
                tokens.append(m.group(0))
        app = ApplicationFactory.by_name(tokens[0])
        args = tokens[1:]
        app.exec(args, None, out)
        # if app == "grep":
        #     if len(args) < 2:
        #         raise ValueError("wrong number of command line arguments")
        #     pattern = args[0]
        #     files = args[1:]
        #     for file in files:
        #         with open(file) as f:
        #             lines = f.readlines()
        #             for line in lines:
        #                 if re.match(pattern, line):
        #                     if len(files) > 1:
        #                         out.append(f"{file}:{line}")
        #                     else:
        #                         out.append(line)


if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    if args_num > 0:
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")
        out = deque()
        eval(sys.argv[2], out)
        while len(out) > 0:
            print(out.popleft(), end="")
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            out = deque()
            eval(cmdline, out)
            while len(out) > 0:
                print(out.popleft(), end="")
