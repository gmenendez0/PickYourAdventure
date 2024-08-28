from http import HTTPStatus

from services.domain.exceptions.GameAlreadyFinishedException import GameAlreadyFinishedException
from services.domain.exceptions.GameAlreadyStartedException import GameAlreadyStartedException
from services.domain.exceptions.GameNotStartedException import GameNotStartedException
from services.domain.exceptions.InvalidOptionIndexException import InvalidOptionIndexException

EXCEPTION_TO_STATUS = {
    str(GameNotStartedException): HTTPStatus.CONFLICT,
    str(GameAlreadyStartedException): HTTPStatus.CONFLICT,
    str(GameAlreadyFinishedException): HTTPStatus.CONFLICT,
    str(InvalidOptionIndexException): HTTPStatus.BAD_REQUEST,
}

def get_http_error_code(exception: Exception) -> HTTPStatus:
    return EXCEPTION_TO_STATUS.get(str(type(exception)), HTTPStatus.INTERNAL_SERVER_ERROR)