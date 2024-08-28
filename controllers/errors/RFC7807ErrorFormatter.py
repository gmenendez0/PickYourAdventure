from http import HTTPStatus

from controllers.errors.ErrorFormatter import ErrorFormatter
from controllers.errors.helpers import get_http_error_code

STANDARD_INTERNAL_SERVER_ERROR_MESSAGE = 'An internal server error occurred. Please try again later.'

class RFC7807ErrorFormatter(ErrorFormatter):
    def format(self, exception: Exception) -> dict:
        status = get_http_error_code(exception)
        title = STANDARD_INTERNAL_SERVER_ERROR_MESSAGE if status == HTTPStatus.INTERNAL_SERVER_ERROR else str(exception)
        err_type = 'about:blank'

        return {'status': status, 'title': title, 'type': err_type}