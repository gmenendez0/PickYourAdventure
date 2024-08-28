from repositories.SQLiteAdventureRepositoryStrategy import SQLiteAdventureRepositoryStrategy
from services.domain.Adventure import Adventure


class AdventureRepository:
    def __init__(self):
        self._strategy = SQLiteAdventureRepositoryStrategy("db.sqlite3")

    def get_by_id(self, adventure_id) -> Adventure:
        """Retrieve an Adventure instance by its ID.

        Args:
            adventure_id (int): The ID of the adventure to retrieve.

        Returns:
            Adventure: The Adventure instance corresponding to the given ID.
        """
        return self._strategy.get_by_id(adventure_id)
