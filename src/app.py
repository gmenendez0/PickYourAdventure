from flask import Flask
from src.controllers.GameController import game_bp, GameController


def create_app():
    main_app = Flask(__name__)
    game_controller = GameController()

    game_bp.add_url_rule(
        "/start", view_func=game_controller.start_adventure, methods=["POST"]
    )
    game_bp.add_url_rule(
        "/choose", view_func=game_controller.choose_path, methods=["POST"]
    )

    main_app.register_blueprint(game_bp, url_prefix="/game")

    return main_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
