from . import *


class ApplicationFactory:
    apps = {
        "cat": cat.Cat(),
        "cd": cd.Cd(),
        "cut": cut.Cut(),
        "echo": echo.Echo(),
        "find": find.Find(),
        "grep": grep.Grep(),
        "head": head.Head(),
        "ls": ls.Ls(),
        "pwd": pwd.Pwd(),
        "sort": sort.Sort(),
        "tail": tail.Tail(),
        "uniq": uniq.Uniq()
    }

    @staticmethod
    def by_name(name: str) -> application.Application:
        if name[0] == "_":
            return unsafe_decorator.UnsafeDecorator(ApplicationFactory.apps[name[1:]])

        return ApplicationFactory.apps[name]
