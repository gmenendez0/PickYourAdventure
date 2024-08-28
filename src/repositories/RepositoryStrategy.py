from abc import ABC, abstractmethod
from typing import Any


class RepositoryStrategy(ABC):
    @abstractmethod
    def get_by_id(self, instance_id: Any) -> Any:
        """Retrieve an instance by its ID.

        Args:
            instance_id (Any): The ID of the instance to retrieve.

        Returns:
            Any: The instance associated with the given ID. The type of the returned
            value depends on the specific repository implementation.
        """
        pass
