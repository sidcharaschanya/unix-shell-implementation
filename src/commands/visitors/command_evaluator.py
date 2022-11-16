from ..impl.pipe import Pipe
from ..impl.seq import Seq


class CommandEvaluator:
    def visit_pipe(self, pipe: Pipe) -> None:
        pass

    def visit_seq(self, seq: Seq) -> None:
        pass
