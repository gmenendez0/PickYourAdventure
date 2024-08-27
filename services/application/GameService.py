from services.application.AdventureService import AdventureService
from services.domain.Adventure import Adventure
from services.domain.Game import Game
from services.dto.GameStatusDto import GameStatusDto

class GameService:
    def __init__(self):
        self._game = Game()
        self._adventureService = AdventureService()

    def start_game(self) -> GameStatusDto:
        first_adventure = self._get_first_adventure()
        self._game.start_game(first_adventure)

        return self._get_game_status_dto()

    def _get_first_adventure(self) -> Adventure:
        return self._adventureService.get_first_adventure()

    def choose_next_adventure(self, index: int) -> GameStatusDto:
        self._game.choose_next_adventure(index)
        return self._get_game_status_dto()

    def _get_game_status_dto(self) -> GameStatusDto:
        return GameStatusDto(self._game.get_current_adventure(), self._game.get_status())
        #return {
        #    "current_adventure": self._game.get_current_adventure_data(),
        #    "status": self._game.get_status().value
        #}
