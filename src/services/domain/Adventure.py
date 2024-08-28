from src.services.domain.exceptions.InvalidOptionIdException import InvalidOptionIdException

class Adventure:
    def __init__(self, description: str, options: list["Adventure"]):
        self._id = id(self)
        self._description = description
        self._options = options

    def get_id(self) -> int:
        """Retrieve the unique identifier of the adventure.

        Returns:
            int: The unique ID of the adventure.
        """
        return self._id

    def get_option(self, adventure_id: int) -> "Adventure":
        """Retrieve an option based on its ID.

        Args:
            adventure_id (int): The ID of the option adventure to retrieve.

        Returns:
            Adventure: The adventure option matching the given ID.

        Raises:
            InvalidOptionIdException: If no option with the given ID is found.
        """
        for option in self._options:
            if option.get_id() == adventure_id:
                return option

        raise InvalidOptionIdException()

    def get_adventure_description_and_options_data(self) -> dict:
        """Retrieve the adventure's description and options data.

        Returns:
            dict: A dictionary containing the adventure's description and options.
        """
        return {
            "description": self._description,
            "options": self._get_options_ids_and_descriptions()
        }

    def _get_options_ids_and_descriptions(self) -> list[dict]:
        """Retrieve the IDs and descriptions of all options.

        Returns:
            list[dict]: A list of dictionaries, each containing the ID and description
            of an option adventure.
        """
        return [option.get_id_and_description() for option in self._options]

    def get_id_and_description(self) -> dict:
        """Retrieve the ID and description of the adventure.

        Returns:
            dict: A dictionary containing the ID and description of the adventure.
        """
        return {
            "id": self._id,
            "description": self._description
        }

    def is_ending_adventure(self) -> bool:
        """Determine if the adventure is an ending adventure.

        An ending adventure has no options.

        Returns:
            bool: True if the adventure has no options, False otherwise.
        """
        return len(self._options) == 0

