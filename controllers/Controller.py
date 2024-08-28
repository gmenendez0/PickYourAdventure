from abc import ABC
from http import HTTPStatus

from flask import Request

from controllers.errors.RFC7807ErrorFormatter import RFC7807ErrorFormatter
from controllers.errors.helpers import get_http_error_code

class Controller(ABC):
    def __init__(self):
        self._error_formatter = RFC7807ErrorFormatter()

    @staticmethod
    def _format_response(data: dict, status_code: HTTPStatus) -> tuple[dict, HTTPStatus]:
        """Format the response data and status code into a tuple.

        Args:
            data (dict): The response data to format.
            status_code (HTTPStatus): The HTTP status code to include in the response.

        Returns:
            tuple[dict, HTTPStatus]: A tuple containing the response data and status code.
        """
        return data, status_code

    def ok_response(self, data: dict) -> tuple[dict, HTTPStatus]:
        """Create a successful response with HTTP status 200 OK.

        Args:
            data (dict): The data to include in the response.

        Returns:
            tuple[dict, HTTPStatus]: A tuple containing the response data and status code (200 OK).
        """
        return self._format_response(data, HTTPStatus.OK)

    def handle_exception(self, exception: Exception) -> tuple[dict, HTTPStatus]:
        """Handle an exception and return a formatted error response.

        Args:
            exception (Exception): The exception to handle.

        Returns:
            tuple[dict, HTTPStatus]: A tuple containing the formatted error data and the corresponding HTTP status code.
        """
        return self._format_response(self._format_exception(exception), get_http_error_code(exception))

    def _format_exception(self, exception: Exception) -> dict:
        """Format an exception using the RFC7807 error formatter.

        Args:
            exception (Exception): The exception to format.

        Returns:
            dict: A dictionary representation of the formatted error.
        """
        return self._error_formatter.format(exception)

    @staticmethod
    def get_request_data(request: Request) -> dict:
        """Extract JSON data from a Flask request.

        Args:
            request (Request): The Flask request object.

        Returns:
            dict: The JSON data extracted from the request.
        """
        return request.json
