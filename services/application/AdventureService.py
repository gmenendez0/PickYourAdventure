from repositories.AdventureRepository import AdventureRepository
from services.domain.Adventure import Adventure

FIRST_ADVENTURE_ID = 1 #TODO Levantar desde .env

class AdventureService:
    def __init__(self):
        self._repository = AdventureRepository()

    def _get_adventure(self, adventure_id: int) -> Adventure:
        pass

    def get_first_adventure(self) -> Adventure:
        return self._get_adventure(FIRST_ADVENTURE_ID)