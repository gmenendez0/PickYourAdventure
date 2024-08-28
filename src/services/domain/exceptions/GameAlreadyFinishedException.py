class GameAlreadyFinishedException(Exception):
    def __init__(self, message="Game has already finished."):
        super().__init__(message)
