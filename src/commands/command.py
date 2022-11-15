from abc import ABC, abstractmethod
from collections import deque
from typing import Optional


class Command(ABC):
    @abstractmethod
    def eval(self, evaluator, input_: Optional[str], out: deque) -> None:
        pass
