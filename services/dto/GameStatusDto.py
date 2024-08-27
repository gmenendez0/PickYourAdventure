from services.domain.Adventure import Adventure
from services.domain.GameStatus import GameStatus

class GameStatusDto:
    def __init__(self, current_adventure: Adventure, status: GameStatus):
        self._current_adventure = current_adventure
        self._status = status