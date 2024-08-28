from http import HTTPStatus

from controllers.errors.ErrorFormatter import ErrorFormatter

class RFC7807ErrorFormatter(ErrorFormatter):
    def format(self, exception: Exception, additional_data: dict) -> dict:
        err_type = additional_data.get('type', 'about:blank')
        status = additional_data.get('status', HTTPStatus.INTERNAL_SERVER_ERROR)

        if not isinstance(status, HTTPStatus):
            status = HTTPStatus.INTERNAL_SERVER_ERROR

        return {
            'type': err_type,
            'title': str(exception),
            'status': str(status),
        }