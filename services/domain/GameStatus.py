from enum import Enum

class GameStatus(Enum):
    NOT_STARTED = 1
    STARTED = 2
    FINISHED = 3

    def __str__(self):
        """Return the string representation of the game status.

        Returns:
            str: The lowercase name of the game status.
        """
        return self.name.lower()