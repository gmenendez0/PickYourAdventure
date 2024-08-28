from src.repositories.AdventureRepository import AdventureRepository
from src.services.domain.Adventure import Adventure

FIRST_ADVENTURE_ID = 1

class AdventureService:
    def __init__(self):
        self._repository = AdventureRepository()

    def _get_adventure(self, adventure_id: int) -> Adventure:
        """Retrieve an adventure by its ID.

        Args:
            adventure_id (int): The ID of the adventure to retrieve.

        Returns:
            Adventure: The adventure corresponding to the given ID.

        Raises:
            ValueError: If no adventure is found with the given ID.
        """
        return self._repository.get_by_id(adventure_id)

    def get_first_adventure(self) -> Adventure:
        """Retrieve the first adventure using a predefined ID.

        Returns:
            Adventure: The adventure with the ID `FIRST_ADVENTURE_ID`.
        """
        return self._get_adventure(FIRST_ADVENTURE_ID)