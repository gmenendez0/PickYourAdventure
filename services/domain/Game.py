from services.domain.Adventure import Adventure
from services.domain.GameStatus import GameStatus
from services.domain.exceptions.GameAlreadyFinishedException import GameAlreadyFinishedException
from services.domain.exceptions.GameAlreadyStartedException import GameAlreadyStartedException
from services.domain.exceptions.GameNotStartedException import GameNotStartedException


class Game:
    def __init__(self):
        self._current_adventure = None
        self._status = GameStatus.NOT_STARTED

    def start_game(self, first_adventure: Adventure) -> None:
        self._validate_game_start()
        self._set_status(GameStatus.STARTED)
        self._set_current_adventure(first_adventure)

    def _validate_game_start(self) -> None:
        if self._game_has_started():
            raise GameAlreadyStartedException()

        if self._game_has_finished():
            raise GameAlreadyFinishedException()

    def _set_status(self, status: GameStatus) -> None:
        self._status = status

    def get_current_adventure(self) -> Adventure:
        return self._current_adventure

    def get_status(self) -> GameStatus:
        return self._status

    def _game_has_started(self) -> bool:
        return self.get_status == GameStatus.STARTED

    def _game_has_finished(self) -> bool:
        return self.get_status == GameStatus.FINISHED

    def choose_next_adventure(self, index: int) -> None:
        self._validate_play()
        self._set_current_adventure(self._current_adventure.get_option(index))

    def _validate_play(self) -> None:
        if not self._game_has_started():
            raise GameNotStartedException()

        if self._game_has_finished():
            raise GameAlreadyFinishedException()

    def _set_current_adventure(self, adventure: Adventure) -> None:
        self._current_adventure = adventure

        if self._current_adventure.is_ending_adventure():
            self._set_status(GameStatus.FINISHED)




