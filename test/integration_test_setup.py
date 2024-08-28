import sqlite3
import os

def initialize_test_database(db_path: str):
    if os.path.exists(db_path):
        os.remove(db_path)

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS adventures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL
    );
    ''')

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

    print("Test database initialized.")

def populate_test_database(db_path: str):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('DELETE FROM adventure_options;')
    cursor.execute('DELETE FROM adventures;')

    cursor.execute('INSERT INTO adventures (description) VALUES (?)',
                   ('Estás en un bosque oscuro. Hay dos caminos frente a ti.',))
    start_adventure_id = cursor.lastrowid

    cursor.execute('INSERT INTO adventures (description) VALUES (?)',
                   ('Te diriges hacia la izquierda, hacia un sendero rocoso.',))
    left_path_id = cursor.lastrowid

    cursor.execute('INSERT INTO adventures (description) VALUES (?)',
                   ('Te diriges hacia la derecha, hacia un río con aguas tranquilas.',))
    right_path_id = cursor.lastrowid

    cursor.execute('INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)',
                   (start_adventure_id, left_path_id))
    cursor.execute('INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)',
                   (start_adventure_id, right_path_id))

    connection.commit()
    connection.close()

    print("Test database populated.")

if __name__ == "__main__":
    test_db_path = 'db.sqlite3'
    initialize_test_database(test_db_path)
    populate_test_database(test_db_path)
