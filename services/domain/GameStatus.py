from enum import Enum

class GameStatus(Enum):
    NOT_STARTED = 1
    STARTED = 2
    FINISHED = 3

    def __str__(self):
        return self.name.lower()