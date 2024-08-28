import unittest
from services.domain.Adventure import Adventure
from services.domain.exceptions.InvalidOptionIdException import InvalidOptionIdException

class TestAdventure(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.option1 = Adventure("Option 1 description", [])
        self.option2 = Adventure("Option 2 description", [])
        self.adventure = Adventure("Main adventure description", [self.option1, self.option2])

    def test_get_id(self):
        """Test that the ID is correctly assigned."""
        self.assertIsInstance(self.adventure.get_id(), int)

    def test_get_option(self):
        """Test retrieving an option by ID."""
        option = self.adventure.get_option(self.option1.get_id())
        self.assertEqual(option.get_id(), self.option1.get_id())
        self.assertEqual(option._description, "Option 1 description")

    def test_get_option_raises_exception_for_invalid_id(self):
        """Test that an exception is raised for invalid option IDs."""
        with self.assertRaises(InvalidOptionIdException):
            self.adventure.get_option(999)

    def test_get_adventure_description_and_options_data(self):
        """Test conversion to dictionary."""
        expected = {
            "description": "Main adventure description",
            "options": [
                {"id": self.option1.get_id(), "description": "Option 1 description"},
                {"id": self.option2.get_id(), "description": "Option 2 description"}
            ]
        }
        self.assertEqual(self.adventure.get_adventure_description_and_options_data(), expected)

if __name__ == "__main__":
    unittest.main()
