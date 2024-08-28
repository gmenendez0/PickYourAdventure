import sqlite3

def initialize_database(db_path: str):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Crear la tabla de aventuras
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS adventures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL
    );
    ''')

    # Crear la tabla de opciones de aventuras
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS adventure_options (
            adventure_id INTEGER NOT NULL,
            option_id INTEGER NOT NULL,
            FOREIGN KEY (adventure_id) REFERENCES adventures(id),
            FOREIGN KEY (option_id) REFERENCES adventures(id),
            PRIMARY KEY (adventure_id, option_id)
        );
    ''')

    connection.commit()
    connection.close()

initialize_database('../db.sqlite3')
