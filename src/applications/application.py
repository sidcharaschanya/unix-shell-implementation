from abc import ABC, abstractmethod
from collections import deque
from typing import Optional


class Application(ABC):
    @abstractmethod
    def exec(self, args: list, input_: Optional[list], out: deque) -> None:
        pass
