from services.domain.Game import Game

class GameService:
    def __init__(self):
        self._game = Game()

    def start_game(self) -> dict:
        first_adventure = None #TODO Cambiar por aventura inicial
        self._game.start_game(first_adventure)

        return self._get_game_status_dto()

    def choose_next_adventure(self, index: int) -> dict:
        self._game.choose_next_adventure(index)
        return self._get_game_status_dto()

    def _get_game_status_dto(self) -> dict:
        #TODO Cambiar por una clase DTO apropiada.
        return {
            "current_adventure": self._game.get_current_adventure_data(),
            "status": self._game.get_status().value
        }
