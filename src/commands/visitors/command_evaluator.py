from collections import deque
from ..impl.pipe import Pipe
from ..impl.seq import Seq
from typing import Optional


class CommandEvaluator:
    def visit_pipe(self, pipe: Pipe, out: deque) -> None:
        temp_out = deque()
        pipe.left.eval(self, None, temp_out)
        pipe.right.eval(self, "".join(temp_out), out)

    def visit_seq(self, seq: Seq, out: deque) -> None:
        seq.left.eval(self, None, out)
        seq.right.eval(self, None, out)
