from repositories.SQLiteAdventureRepositoryStrategy import SQLiteAdventureRepositoryStrategy
from services.domain.Adventure import Adventure


class AdventureRepository:
    def __init__(self):
        self._strategy = SQLiteAdventureRepositoryStrategy("db.sqlite3")

    def get_by_id(self, adventure_id) -> Adventure:
        return self._strategy.get_by_id(adventure_id)
