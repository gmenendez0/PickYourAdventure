from src.controllers.Controller import Controller
from src.controllers.exceptions.InvalidRequestDataException import (
    InvalidRequestDataException,
)
from src.services.application.GameService import GameService

from flask import Blueprint, request

game_bp = Blueprint("game", __name__)


class GameController(Controller):
    def __init__(self):
        super().__init__()
        self._game_service = GameService()

    def start_adventure(self):
        """Handle the request to start a new adventure.

        Returns:
            tuple[dict, HTTPStatus]: A tuple containing the game status and HTTP status code.
        """
        try:
            game_status_dto = self._game_service.start_game()
            return self.ok_response(game_status_dto.to_dict())
        except Exception as e:
            return self.handle_exception(e)

    def choose_path(self):
        """Handle the request to choose a path in the game.

        Returns:
            tuple[dict, HTTPStatus]: A tuple containing the updated game status and HTTP status code.
        """
        try:
            data = self.get_request_data(request)
            choice = data.get("choiceId")

            if choice is None:
                raise InvalidRequestDataException("Field {choiceId} cannot be empty.")

            game_status_dto = self._game_service.choose_next_adventure(choice)
            return self.ok_response(game_status_dto.to_dict())
        except Exception as e:
            return self.handle_exception(e)
