from services.domain.Adventure import Adventure
from services.domain.GameStatus import GameStatus

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
            raise Exception("Game has already started.") #TODO Cambiar por excepción personalizada

    def _set_status(self, status: GameStatus) -> None:
        self._status = status

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
        if self._game_has_finished():
            raise Exception("Game has already finished.") #TODO Cambiar por excepción personalizada

    def _set_current_adventure(self, adventure: Adventure) -> None:
        self._current_adventure = adventure

        if self._current_adventure.is_ending_adventure():
            self._set_status(GameStatus.FINISHED)

    def get_current_adventure_data(self) -> dict:
        return self._current_adventure.get_adventure_description_and_options_data()




