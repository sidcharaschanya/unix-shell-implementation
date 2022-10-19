from abc import ABC, abstractmethod
from collections import deque


class Application(ABC):
    @abstractmethod
    def exec(self, args: list, out: deque) -> deque:
        pass
