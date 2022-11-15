from abc import ABC, abstractmethod
from collections import deque
from typing import Optional
from .visitors.evaluator import Evaluator


class Command(ABC):
    @abstractmethod
    def eval(self, e: Evaluator, input_: Optional[str], out: deque) -> None:
        pass
