from collections import deque
from commands.command_visitor import CommandVisitor
import os
import sys


def eval(cmdline: str, out: deque) -> None:
    CommandVisitor.parse(cmdline).eval(None, out)


def run(cmdline: str) -> None:
    out = deque()
    eval(cmdline, out)

    while len(out) > 0:
        print(out.popleft(), end="")


def non_interactive_mode(num_args: int) -> None:
    if num_args != 2:
        raise ValueError("wrong number of command line arguments")

    if sys.argv[1] != "-c":
        raise ValueError(f"unexpected command line argument {sys.argv[1]}")

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
