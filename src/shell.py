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


def run(cmdline: str) -> None:
    out = deque()
    eval(cmdline, out)

    while len(out) > 0:
        print(out.popleft(), end="")


def non_interactive_mode(num_args: int) -> None:
    if num_args != 2:
        raise ValueError("shell: wrong number of command line arguments")

    if sys.argv[1] != "-c":
        raise ValueError(f"shell: unexpected command line argument {sys.argv[1]}")

    run(sys.argv[2])


def interactive_mode() -> None:
    while True:
        print(os.getcwd() + "> ", end="")
        run(input())


def main() -> None:
    num_args = len(sys.argv) - 1

    if num_args > 0:
        non_interactive_mode(num_args)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
