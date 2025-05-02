from abc import ABC, abstractmethod
from typing import List

class BaseProvider(ABC):
    def __init__(self, config: dict):
        self.config = config

    @abstractmethod
    def generate(self, prompt: str, context: List[str] = []) -> str:
        pass
