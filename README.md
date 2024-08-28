# PickYourAdventure

**PickYourAdventure** is an interactive text-based game built with Flask and SQLite, where users can embark on adventures and make decisions that affect the outcome of the game.

## Project Structure

- **`src/`**: Contains the Flask application and controllers.
  - **`app.py`**: Main file to start the application.
  - **`controllers/`**: Contains controllers for handling API routes.
  - **`services/`**: Contains business logic.
    - **`services/application`**: Contains logic for executing use cases and interacting with the database.
    - **`services/domain`**: Contains the game's domain entities and models.
    - **`services/dto`**: Contains data transfer objects.
  - **`repositories/`**: Contains implementations for accessing the database.

- **`tests/`**: Contains unit and integration tests for the application.
  - **`test_game.py`**: Unit tests for game logic.
  - **`test_game_controller.py`**: Tests for API controllers.

- **`db.sqlite3`**: SQLite database file used by the application.

## Requirements

- Python 3.6 or higher

## Installation

1. **Clone the repository**

2. **Create a virtual environment and install dependencies**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Initialize the database**:

    Run the following script to create and initialize the database:

    ```bash
    python scripts/initializeDatabase.py
    ```

## Usage

To start the application, run:

```bash
python src/app.py
```

## API Documentation

### POST /game/start

Initiates a new adventure and returns the initial state with available options. 
Game must not be "started" or "finished".

#### Request

- **URL:** `/game/start`
- **Method:** `POST`
- **Content-Type:** `application/json`

#### Response

- **Status Code:** `200 OK`

#### Response Body

The response body contains the following JSON structure:

```json
{
    "current_adventure": {
        "description": "Estás en un bosque oscuro. Hay dos caminos frente a ti.",
        "options": [
            {
                "description": "Te diriges hacia la izquierda, hacia un sendero rocoso.",
                "id": 140374155295952
            },
            {
                "description": "Te diriges hacia la derecha, hacia un río con aguas tranquilas.",
                "id": 140374155296048
            }
        ]
    },
    "status": "started"
}
```

### POST /game/choose

Chooses an option in the current adventure and returns the resulting state.
- Game must be "started".
- "choiceId" must be a valid option ID, returned by the previous API call to `/game/start` or `/game/choose`.



#### Request

- **URL:** `/game/choose`
- **Method:** `POST`
- **Content-Type:** `application/json`

#### Request Body

The request body must contain the following JSON structure:

```json
{
    "choiceId": 140255887785120
}
```

#### Response body
```json
{
    "current_adventure": {
        "description": "Te diriges hacia la izquierda, hacia un sendero rocoso.",
        "options": [
            {
                "description": "Encuentras una cueva. Puedes entrar o seguir adelante.",
                "id": 140255887785312
            },
            {
                "description": "Sigues subiendo por el sendero hasta llegar a la cima de una colina.",
                "id": 140255887785456
            }
        ]
    },
    "status": "started"
}
```
