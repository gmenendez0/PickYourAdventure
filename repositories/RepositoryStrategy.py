from abc import ABC, abstractmethod
from typing import Any

class RepositoryStrategy(ABC):
    @abstractmethod
    def get_by_id(self, instance_id: Any) -> Any:
        pass