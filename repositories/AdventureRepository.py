from repositories.SQLiteAdventureRepositoryStrategy import SQLiteAdventureRepositoryStrategy

class AdventureRepository:
    def __init__(self):
        self._strategy = SQLiteAdventureRepositoryStrategy("db.sqlite3")

    def get_by_id(self, adventure_id):
        self._strategy.get_by_id(adventure_id)
