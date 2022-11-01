from .application import Application
from .impl.cat import Cat
from .impl.cd import Cd
from .impl.cut import Cut
from .impl.echo import Echo
from .impl.find import Find
from .impl.grep import Grep
from .impl.head import Head
from .impl.ls import Ls
from .impl.pwd import Pwd
from .impl.sort import Sort
from .impl.tail import Tail
from .impl.uniq import Uniq
from .impl.unsafe_decorator import UnsafeDecorator


class ApplicationFactory:
    __apps = {
        "cat": Cat(),
        "cd": Cd(),
        "cut": Cut(),
        "echo": Echo(),
        "find": Find(),
        "grep": Grep(),
        "head": Head(),
        "ls": Ls(),
        "pwd": Pwd(),
        "sort": Sort(),
        "tail": Tail(),
        "uniq": Uniq()
    }

    @staticmethod
    def by_name(name: str) -> Application:
        if name[0] == "_":
            return UnsafeDecorator(ApplicationFactory.__apps[name[1:]])

        return ApplicationFactory.__apps[name]
