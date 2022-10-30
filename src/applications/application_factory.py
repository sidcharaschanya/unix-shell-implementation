from .application import Application
import impl


class ApplicationFactory:
    apps = {
        "cat": impl.cat.Cat(),
        "cd": impl.cd.Cd(),
        "cut": impl.cut.Cut(),
        "echo": impl.echo.Echo(),
        "find": impl.find.Find(),
        "grep": impl.grep.Grep(),
        "head": impl.head.Head(),
        "ls": impl.ls.Ls(),
        "pwd": impl.pwd.Pwd(),
        "sort": impl.sort.Sort(),
        "tail": impl.tail.Tail(),
        "uniq": impl.uniq.Uniq()
    }

    @staticmethod
    def by_name(name: str) -> Application:
        if name[0] == "_":
            return impl.unsafe_decorator.UnsafeDecorator(ApplicationFactory.apps[name[1:]])

        return ApplicationFactory.apps[name]
