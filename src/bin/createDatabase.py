import sqlite3
import os


def initialize_database(db_path: str):
    if os.path.exists(db_path):
        print(f"La base de datos {db_path} ya existe. Eliminando el archivo...")
        os.remove(db_path)
        print(f"Archivo {db_path} eliminado.")

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS adventures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS adventure_options (
        adventure_id INTEGER NOT NULL,
        option_id INTEGER NOT NULL,
        FOREIGN KEY (adventure_id) REFERENCES adventures(id),
        FOREIGN KEY (option_id) REFERENCES adventures(id),
        PRIMARY KEY (adventure_id, option_id)
    );
    """
    )

    connection.commit()
    connection.close()

    print("Base de datos inicializada con nuevas tablas.")


initialize_database("../db.sqlite3")
