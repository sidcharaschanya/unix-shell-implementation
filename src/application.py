from abc import ABC, abstractmethod
from collections import deque


class Application(ABC):
    @abstractmethod
    def exec(self, args: list, input_: deque, out: deque) -> deque:
        pass
