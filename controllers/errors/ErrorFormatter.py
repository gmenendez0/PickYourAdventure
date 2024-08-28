from abc import ABC, abstractmethod

class ErrorFormatter(ABC):
    @abstractmethod
    def format(self, exception: Exception, additional_data: dict) -> dict:
        pass