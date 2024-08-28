from abc import ABC, abstractmethod

class ErrorFormatter(ABC):
    @abstractmethod
    def format(self, exception: Exception) -> dict:
        """Format an exception into a dictionary.

        This method must be implemented by subclasses to provide specific
        formatting logic for different types of exceptions.

        Args:
            exception (Exception): The exception to be formatted.

        Returns:
            dict: A dictionary representation of the formatted error.
        """
        pass