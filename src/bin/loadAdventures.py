import sqlite3

DB_PATH = "../db.sqlite3"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_adventures():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM adventure_options;")
    cursor.execute("DELETE FROM adventures;")

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        ("Estás en un bosque oscuro. Hay dos caminos frente a ti.",),
    )
    start_adventure_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        ("Te diriges hacia la izquierda, hacia un sendero rocoso.",),
    )
    left_path_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        ("Te diriges hacia la derecha, hacia un río con aguas tranquilas.",),
    )
    right_path_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)",
        (start_adventure_id, left_path_id),
    )
    cursor.execute(
        "INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)",
        (start_adventure_id, right_path_id),
    )

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        ("Encuentras una cueva. Puedes entrar o seguir adelante.",),
    )
    cave_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        ("Sigues subiendo por el sendero hasta llegar a la cima de una colina.",),
    )
    hilltop_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)",
        (left_path_id, cave_id),
    )
    cursor.execute(
        "INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)",
        (left_path_id, hilltop_id),
    )

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        ("Decides cruzar el río nadando.",),
    )
    swim_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        ("Sigues el curso del río hacia una cascada.",),
    )
    waterfall_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)",
        (right_path_id, swim_id),
    )
    cursor.execute(
        "INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)",
        (right_path_id, waterfall_id),
    )

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        ("Entras en la cueva y encuentras un tesoro brillante. ¡Has ganado!",),
    )
    treasure_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        ("Sigues adelante por el sendero y te pierdes en la oscuridad. ¡Has perdido!",),
    )
    lost_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        (
            "Nadas a través del río y encuentras un bote que te lleva a casa. ¡Has ganado!",
        ),
    )
    boat_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventures (description) VALUES (?)",
        ("Sigues el curso del río hasta la cascada y te caes. ¡Has perdido!",),
    )
    fall_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)",
        (cave_id, treasure_id),
    )
    cursor.execute(
        "INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)",
        (hilltop_id, lost_id),
    )
    cursor.execute(
        "INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)",
        (swim_id, boat_id),
    )
    cursor.execute(
        "INSERT INTO adventure_options (adventure_id, option_id) VALUES (?, ?)",
        (waterfall_id, fall_id),
    )

    connection.commit()
    connection.close()

    print("Base de datos inicializada con aventuras y finales.")


initialize_adventures()
