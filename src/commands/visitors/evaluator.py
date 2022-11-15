from collections import deque
from ..impl.pipe import Pipe
from ..impl.seq import Seq
from typing import Optional


class Evaluator:
    def visit_pipe(self, pipe: Pipe, input_: Optional[str], out: deque) -> None:
        pass

    def visit_seq(self, seq: Seq, input_: Optional[str], out: deque) -> None:
        pass
