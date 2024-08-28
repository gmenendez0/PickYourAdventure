from sqlite3 import Cursor

from repositories.RepositoryStrategy import RepositoryStrategy
import sqlite3

from services.domain.Adventure import Adventure

class SQLiteAdventureRepositoryStrategy(RepositoryStrategy):
    def __init__(self, db_path: str):
        self._db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        """Establish a connection to the SQLite database.

        Returns:
            sqlite3.Connection: The SQLite connection object.

        Notes:
            Ensure to handle exceptions when connecting to the database in production.
        """
        return sqlite3.connect(self._db_path)

    @staticmethod
    def _close_connection(connection: sqlite3.Connection) -> None:
        """Close the SQLite database connection.

        Args:
            connection (sqlite3.Connection): The connection object to close.
        """
        connection.close()

    def get_by_id(self, instance_id: int) -> Adventure:
        """Retrieve an Adventure instance by its ID.

        Args:
            instance_id (int): The ID of the adventure to retrieve.

        Returns:
            Adventure: The Adventure instance corresponding to the given ID.

        Raises:
            ValueError: If no adventure is found with the provided ID.
        """
        connection = self._get_connection()
        cursor = connection.cursor()

        adventure = self._get_adventure_by_id(instance_id, cursor)

        self._close_connection(connection)
        return adventure

    def _get_adventure_by_id(self, adventure_id: int, cursor: Cursor) -> Adventure:
        """Retrieve an Adventure instance and its options by adventure ID.

        Args:
            adventure_id (int): The ID of the adventure to retrieve.
            cursor (Cursor): The SQLite cursor object to execute queries.

        Returns:
            Adventure: The Adventure instance with the specified ID.

        Raises:
            ValueError: If no adventure is found with the provided ID.

        Notes:
            This method should only be used if there are no cycles in the graph of adventures
        """
        cursor.execute('SELECT description FROM adventures WHERE id = ?', (adventure_id,))
        result = cursor.fetchone()

        if result is None:
            raise ValueError(f"No adventure found with id {adventure_id}")

        description = result[0]

        cursor.execute('SELECT option_id FROM adventure_options WHERE adventure_id = ?', (adventure_id,))
        options_result = cursor.fetchall()

        options = [self._get_adventure_by_id(option_id[0], cursor) for option_id in options_result]

        return Adventure(description, options)


