from src.services.application.AdventureService import AdventureService
from src.services.domain.Adventure import Adventure
from src.services.domain.Game import Game
from src.services.dto.GameStatusDto import GameStatusDto

class GameService:
    def __init__(self):
        self._game = Game()
        self._adventureService = AdventureService()

    def start_game(self) -> GameStatusDto:
        """Start the game with the first adventure.

        Retrieves the first adventure from the AdventureService, starts the game
        with that adventure, and returns the current game status as a GameStatusDto.

        Returns:
            GameStatusDto: Data transfer object containing the current adventure and game status.
        """
        first_adventure = self._get_first_adventure()
        self._game.start_game(first_adventure)

        return self._get_game_status_dto()

    def _get_first_adventure(self) -> Adventure:
        """Retrieve the first adventure from the AdventureService.

        Returns:
            Adventure: The first adventure to be used when starting the game.
        """
        return self._adventureService.get_first_adventure()

    def choose_next_adventure(self, adventure_id: int) -> GameStatusDto:
        """Choose the next adventure based on the provided adventure ID.

        Updates the current adventure in the game with the chosen one and returns
        the updated game status as a GameStatusDto.

        Args:
            adventure_id (int): The ID of the adventure to be chosen.

        Returns:
            GameStatusDto: Data transfer object containing the updated adventure and game status.
        """
        self._game.choose_next_adventure(adventure_id)
        return self._get_game_status_dto()

    def _get_game_status_dto(self) -> GameStatusDto:
        """Create a GameStatusDto from the current game state.

        Returns:
            GameStatusDto: Data transfer object containing the current adventure and game status.
        """
        return GameStatusDto(self._game.get_current_adventure(), self._game.get_status())
