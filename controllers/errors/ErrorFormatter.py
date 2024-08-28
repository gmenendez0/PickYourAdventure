from abc import ABC, abstractmethod

class ErrorFormatter(ABC):
    @abstractmethod
    def format(self, exception: Exception) -> dict:
        pass