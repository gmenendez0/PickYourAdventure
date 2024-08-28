import unittest
from app import create_app

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test database."""
        import integration_test_setup
        integration_test_setup.initialize_test_database('db.sqlite3')
        integration_test_setup.populate_test_database('db.sqlite3')

    def setUp(self):
        """Set up the test client and other necessary objects."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_start_and_choose_path(self):
        """Test the /choose endpoint with valid data."""
        # First, start the game to get a valid adventure ID
        start_response = self.client.post('/game/start')
        assert start_response.status_code == 200
        start_data = start_response.get_json()

        # Extract the ID from the options
        options = start_data['current_adventure']['options']
        assert len(options) > 0
        first_option_id = options[0]['id']

        # Now, choose the adventure
        choose_response = self.client.post('/game/choose', json={'choiceId': first_option_id})
        assert choose_response.status_code == 200
        choose_data = choose_response.get_json()

        assert 'current_adventure' in choose_data
        assert 'description' in choose_data['current_adventure']
        assert 'options' in choose_data['current_adventure']
        assert 'status' in choose_data
        assert choose_data['status'] == 'finished'

        adventure = choose_data['current_adventure']
        assert adventure['description'] == 'Te diriges hacia la izquierda, hacia un sendero rocoso.'
        assert len(adventure['options']) == 0

    @classmethod
    def tearDownClass(cls):
        """Clean up the test database."""
        import os
        os.remove('db.sqlite3')

if __name__ == '__main__':
    unittest.main()
