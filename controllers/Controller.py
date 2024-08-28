from abc import ABC
from http import HTTPStatus

from controllers.errors.RFC7807ErrorFormatter import RFC7807ErrorFormatter
from controllers.errors.helpers import get_http_error_code

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
        return self._format_response(self._format_exception(exception), get_http_error_code(exception))

    def _format_exception(self, exception: Exception) -> dict:
        return self._error_formatter.format(exception)
