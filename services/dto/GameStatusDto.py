from services.domain.Adventure import Adventure
from services.domain.GameStatus import GameStatus

class GameStatusDto:
    def __init__(self, current_adventure: Adventure, status: GameStatus):
        self._current_adventure = current_adventure
        self._status = status

    def to_dict(self) -> dict:
        """Convert the GameStatusDto into a dictionary representation.

        Returns:
            dict: A dictionary containing the current adventure's description and options,
                  and the game status as a string.
        """
        return {
            "current_adventure": self._current_adventure.get_adventure_description_and_options_data(),
            "status": self._status.__str__()
        }