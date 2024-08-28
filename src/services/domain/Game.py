from src.services.domain.Adventure import Adventure
from src.services.domain.GameStatus import GameStatus
from src.services.domain.exceptions.GameAlreadyFinishedException import (
    GameAlreadyFinishedException,
)
from src.services.domain.exceptions.GameAlreadyStartedException import (
    GameAlreadyStartedException,
)
from src.services.domain.exceptions.GameNotStartedException import (
    GameNotStartedException,
)
from src.services.domain.exceptions.InvalidAdventureException import (
    InvalidAdventureException,
)


class Game:
    def __init__(self):
        self._current_adventure = None
        self._status = GameStatus.NOT_STARTED

    def start_game(self, first_adventure: Adventure) -> None:
        """Start the game with the given first adventure.

        Args:
            first_adventure (Adventure): The adventure to start the game with.

        Raises:
            GameAlreadyStartedException: If the game has already started.
            GameAlreadyFinishedException: If the game has already finished.
        """
        self._validate_game_start()
        self._set_status(GameStatus.STARTED)
        self._set_current_adventure(first_adventure)

    def _validate_game_start(self) -> None:
        """Validate if the game can be started.

        Raises:
            GameAlreadyStartedException: If the game has already started.
            GameAlreadyFinishedException: If the game has already finished.
        """
        if self._game_has_started():
            raise GameAlreadyStartedException()

        if self._game_has_finished():
            raise GameAlreadyFinishedException()

    def _set_status(self, status: GameStatus) -> None:
        """Set the current status of the game.

        Args:
            status (GameStatus): The status to set.
        """
        self._status = status

    def get_current_adventure(self) -> Adventure:
        """Retrieve the current adventure.

        Returns:
            Adventure: The current adventure of the game.
        """
        return self._current_adventure

    def get_status(self) -> GameStatus:
        """Retrieve the current status of the game.

        Returns:
            GameStatus: The current status of the game.
        """
        return self._status

    def _game_has_started(self) -> bool:
        """Check if the game has started.

        Returns:
            bool: True if the game has started, False otherwise.
        """
        return self.get_status() == GameStatus.STARTED

    def _game_has_finished(self) -> bool:
        """Check if the game has finished.

        Returns:
            bool: True if the game has finished, False otherwise.
        """
        return self.get_status() == GameStatus.FINISHED

    def choose_next_adventure(self, adventure_id: int) -> None:
        """Choose the next adventure based on the given ID.

        Args:
            adventure_id (int): The ID of the adventure to choose.

        Raises:
            GameAlreadyFinishedException: If the game has already finished.
            GameNotStartedException: If the game has not started.
            InvalidOptionIdException: If the adventure option ID is invalid.
        """
        self._validate_play()
        self._set_current_adventure(self._current_adventure.get_option(adventure_id))

    def _validate_play(self) -> None:
        """Validate if the game can proceed with selecting the next adventure.

        Raises:
            GameAlreadyFinishedException: If the game has already finished.
            GameNotStartedException: If the game has not started.
        """
        if self._game_has_finished():
            raise GameAlreadyFinishedException()

        if not self._game_has_started():
            raise GameNotStartedException()

    def _set_current_adventure(self, adventure: Adventure) -> None:
        """Set the current adventure for the game.

        Args:
            adventure (Adventure): The adventure to set as the current adventure.

        Raises:
            InvalidAdventureException: If the adventure is None.
        """
        if adventure is None:
            raise InvalidAdventureException("Adventure cannot be None")

        self._current_adventure = adventure

        if self._current_adventure.is_ending_adventure():
            self._set_status(GameStatus.FINISHED)
