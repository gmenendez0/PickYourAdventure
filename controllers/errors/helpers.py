from http import HTTPStatus

from controllers.exceptions.InvalidRequestDataException import InvalidRequestDataException
from services.domain.exceptions.GameAlreadyFinishedException import GameAlreadyFinishedException
from services.domain.exceptions.GameAlreadyStartedException import GameAlreadyStartedException
from services.domain.exceptions.GameNotStartedException import GameNotStartedException
from services.domain.exceptions.InvalidAdventureException import InvalidAdventureException
from services.domain.exceptions.InvalidOptionIdException import InvalidOptionIdException

EXCEPTION_TO_STATUS = {
    str(GameNotStartedException): HTTPStatus.CONFLICT,
    str(GameAlreadyStartedException): HTTPStatus.CONFLICT,
    str(GameAlreadyFinishedException): HTTPStatus.CONFLICT,
    str(InvalidOptionIdException): HTTPStatus.BAD_REQUEST,
    str(InvalidAdventureException): HTTPStatus.INTERNAL_SERVER_ERROR,
    str(InvalidRequestDataException): HTTPStatus.BAD_REQUEST
}

def get_http_error_code(exception: Exception) -> HTTPStatus:
    return EXCEPTION_TO_STATUS.get(str(type(exception)), HTTPStatus.INTERNAL_SERVER_ERROR)