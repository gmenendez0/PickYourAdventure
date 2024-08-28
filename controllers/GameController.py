from controllers.Controller import Controller
from services.application.GameService import GameService

from flask import Blueprint, request

game_bp = Blueprint('game', __name__)

class GameController(Controller):
    def __init__(self):
        super().__init__()
        self._game_service = GameService()

    def start_adventure(self):
        try:
            game_status_dto = self._game_service.start_game()
            return self.ok_response(game_status_dto.to_dict())
        except Exception as e:
            self.handle_exception(e)

    def choose_path(self):
        try:
            data = self.get_request_data(request)
            choice = data.get('choiceId')

            game_status_dto = self._game_service.choose_next_adventure(choice)
            return self.ok_response(game_status_dto.to_dict())
        except Exception as e:
            self.handle_exception(e)