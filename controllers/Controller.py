from abc import ABC
from http import HTTPStatus

from controllers.errors.RFC7807ErrorFormatter import RFC7807ErrorFormatter
from services.domain.exceptions.GameAlreadyFinishedException import GameAlreadyFinishedException
from services.domain.exceptions.GameHasAlreadyStartedException import GameAlreadyStartedException
from services.domain.exceptions.GameNotStartedException import GameNotStartedException
from services.domain.exceptions.InvalidOptionIndexException import InvalidOptionIndexError

STANDARD_INTERNAL_SERVER_ERROR_MESSAGE = 'An internal server error occurred. Please try again later.'

class Controller(ABC):
    def __init__(self):
        self._error_formatter = RFC7807ErrorFormatter()

    @staticmethod
    def _format_response(data: dict, status_code: HTTPStatus) -> tuple[dict, HTTPStatus]:
        return data, status_code

    def ok_response(self, data: dict) -> tuple[dict, HTTPStatus]:
        return self._format_response(data, HTTPStatus.OK)

    def internal_server_error_response(self, data: dict) -> tuple[dict, HTTPStatus]:
        return self._format_response(data, HTTPStatus.INTERNAL_SERVER_ERROR)

    def bad_request_response(self, data: dict) -> tuple[dict, HTTPStatus]:
        return self._format_response(data, HTTPStatus.BAD_REQUEST)

    def conflict_response(self, data: dict) -> tuple[dict, HTTPStatus]:
        return self._format_response(data, HTTPStatus.CONFLICT)

    def handle_exception(self, exception: Exception) -> tuple[dict, HTTPStatus]:
        if isinstance(exception, GameNotStartedException):
            return self.conflict_response(self._format_exception(exception, {'status': HTTPStatus.CONFLICT}))
        elif isinstance(exception, GameAlreadyStartedException):
            return self.conflict_response(self._format_exception(exception, {'status': HTTPStatus.CONFLICT}))
        elif isinstance(exception, GameAlreadyFinishedException):
            return self.conflict_response(self._format_exception(exception, {'status': HTTPStatus.CONFLICT}))
        elif isinstance(exception, InvalidOptionIndexError):
            return self.bad_request_response(self._format_exception(exception, {'status': HTTPStatus.BAD_REQUEST}))
        else:
            return self.internal_server_error_response(self._format_exception(exception, {'status': HTTPStatus.INTERNAL_SERVER_ERROR, 'title': STANDARD_INTERNAL_SERVER_ERROR_MESSAGE}))

    def _format_exception(self, exception: Exception, additional_data: dict) -> dict:
        return self._error_formatter.format(exception, additional_data)
