from services.domain.Adventure import Adventure
from services.domain.GameStatus import GameStatus

class GameStatusDto:
    def __init__(self, current_adventure: Adventure, status: GameStatus):
        self._current_adventure = current_adventure
        self._status = status

    def to_dict(self) -> dict:
        return {
            "current_adventure": self._current_adventure.get_adventure_description_and_options_data(),
            "status": self._status.value
        }