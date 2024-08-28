from services.domain.exceptions.InvalidOptionIdException import InvalidOptionIdException

class Adventure:
    def __init__(self, description: str, options: list["Adventure"]):
        self._id = id(self)
        self._description = description
        self._options = options

    def get_id(self) -> int:
        return self._id

    def get_option(self, adventure_id: int) -> "Adventure":
        for option in self._options:
            if option.get_id() == adventure_id:
                return option

        raise InvalidOptionIdException()

    def get_adventure_description_and_options_data(self) -> dict:
        return {
            "description": self._description,
            "options": self._get_options_ids_and_descriptions()
        }

    def _get_options_ids_and_descriptions(self) -> list[dict]:
        return [option.get_id_and_description() for option in self._options]

    def get_id_and_description(self) -> dict:
        return {
            "id": self._id,
            "description": self._description
        }

    def is_ending_adventure(self) -> bool:
        return len(self._options) == 0

