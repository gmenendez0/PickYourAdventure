import unittest
from services.domain.Adventure import Adventure
from services.domain.Game import Game
from services.domain.GameStatus import GameStatus
from services.domain.exceptions.GameAlreadyFinishedException import GameAlreadyFinishedException
from services.domain.exceptions.GameAlreadyStartedException import GameAlreadyStartedException
from services.domain.exceptions.GameNotStartedException import GameNotStartedException
from services.domain.exceptions.InvalidAdventureException import InvalidAdventureException

class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.game = Game()
        self.adventure = Adventure("Adventure description", [])

    def test_start_game(self):
        """Test starting the game."""
        option_adventure = Adventure("Option adventure description", [])
        self.adventure._options.append(option_adventure)
        self.game.start_game(self.adventure)
        self.assertEqual(self.game.get_status(), GameStatus.STARTED)
        self.assertEqual(self.game.get_current_adventure(), self.adventure)

    def test_start_game_raises_exception_if_already_started(self):
        """Test that an exception is raised if the game is already started."""
        option_adventure = Adventure("Option adventure description", [])
        self.adventure._options.append(option_adventure)
        self.game.start_game(self.adventure)

        with self.assertRaises(GameAlreadyStartedException):
            self.game.start_game(self.adventure)

    def test_choose_next_adventure(self):
        """Test choosing the next adventure."""
        option_adventure = Adventure("Option adventure description", [])
        self.adventure._options.append(option_adventure)
        self.game.start_game(self.adventure)
        self.game.choose_next_adventure(option_adventure.get_id())
        self.assertEqual(self.game.get_current_adventure(), option_adventure)

    def test_choose_next_adventure_raises_exception_if_game_not_started(self):
        """Test that an exception is raised if the game is not started."""
        with self.assertRaises(GameNotStartedException):
            self.game.choose_next_adventure(1)

    def test_choose_next_adventure_raises_exception_if_game_finished(self):
        """Test that an exception is raised if the game is finished."""
        self.game.start_game(self.adventure)
        with self.assertRaises(GameAlreadyFinishedException):
            self.game.choose_next_adventure(1)

    def test_set_current_adventure_raises_exception_if_none(self):
        """Test that an exception is raised if the adventure is None."""
        self.game.start_game(self.adventure)
        with self.assertRaises(InvalidAdventureException):
            self.game._set_current_adventure(None)

if __name__ == "__main__":
    unittest.main()
