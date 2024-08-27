class GameNotStartedException(Exception):
    def __init__(self, message = "The game has not begun yet."):
        super().__init__(message)