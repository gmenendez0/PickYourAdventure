class GameAlreadyStartedException(Exception):
    def __init__(self, message="The game has already begun."):
        super().__init__(message)
