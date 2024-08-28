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

- **`db.sqlite3`**: SQLite database file used by the application.

## Improvement Point:

1. **Loading the First Adventure:**
   - Upon starting the application, the first adventure is loaded into memory, which in turn recursively loads all other adventures in the graph. This leads to the following two pain points:
   
     a. **Memory Performance:** Although the references to higher hierarchy nodes will be lost as the game progresses, freeing up memory, initially, the entire adventure graph will be loaded into memory. This could be suboptimal in terms of performance.

     b. **Server Startup Delay:** Since the entire graph needs to be loaded into memory to start the game, there might be a delay in server startup due to the large number of read operations that need to be performed against the database.


## Requirements

- Python 3.6 or higher

## Installation

1. **Clone the repository and cd to PickYourAdventure directory**

2. **Create a virtual environment and install dependencies**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Initialize the database**:

    Run the following script to create and initialize the database:

    ```bash
    python src/bin/initializeDatabase.py
    ```

## Usage

To start the application, run:

```bash
python app.py
```

## API Documentation

### Default exposed Port: 5000

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

To run unit tests, set the `PYTHONPATH` environment variable to reference the `PickYourAdventure` directory. Example:

```bash
export PYTHONPATH=$PYTHONPATH:/home/user123/PickYourAdventure
cd /home/user123/PickYourAdventure
python3 test/TestAdventure.py
```
