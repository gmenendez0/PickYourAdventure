from sqlite3 import Cursor

from repositories.RepositoryStrategy import RepositoryStrategy
import sqlite3

from services.domain.Adventure import Adventure

def _close_connection(connection: sqlite3.Connection) -> None:
    connection.close()

class SQLiteAdventureRepositoryStrategy(RepositoryStrategy):
    def __init__(self, table_name: str, db_path: str):
        self._table_name = table_name
        self._db_path = db_path

    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self._db_path) #Chequear si se conecta bien con un try except

    def get_by_id(self, instance_id: int):
        connection = self._get_connection()
        cursor = connection.cursor()

        adventure = self._get_adventure_by_id(instance_id, cursor)

        _close_connection(connection)
        return adventure

    #NO PUEDE HABER CICLOS DE NINGUN TIPO EN EL GRAFO DE AVENTURAS O CAE EN UNA RECURSION INFINITA
    def _get_adventure_by_id(self, adventure_id: int, cursor: Cursor) -> Adventure:
        # Primero obtengo la descripcion de la aventura
        cursor.execute('SELECT description FROM adventures WHERE id = ?', (adventure_id,))
        result = cursor.fetchone()

        #Si no se encontro result, es que la aventura no esta en la db
        if result is None:
            raise ValueError(f"No adventure found with id {adventure_id}")

        #Retriveo la descripcion del resultado
        description = result[0]

        # Obtengo las opciones
        cursor.execute('SELECT option_id FROM adventure_options WHERE adventure_id = ?', (adventure_id,))
        options_result = cursor.fetchall()

        options = [self._get_adventure_by_id(option_id[0], cursor) for option_id in options_result]

        return Adventure(description, options)


