import logging
import sys

from rest_framework import status as rest_status

from apps.common.utils.sentry_service import SentryService


class ValidationErrorsToSentryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        get_data = request.GET
        post_body_data = request.POST
        if hasattr(response, 'data'):
            response_data = response.data
        else:
            response_data = response.content
        if rest_status.is_client_error(response.status_code):
            extras = {
                'GET': get_data,
                'POST': post_body_data,
                'response': response_data,
            }
            if hasattr(response, '_sys_exc_info'):
                exc_info = response._sys_exc_info
            else:
                try:
                    # hack to generate exc_info for Sentry
                    raise Exception('Validation Error')
                except Exception:
                    exc_info = sys.exc_info()

            extras['exc_info'] = exc_info
            SentryService().capture_message(
                message='Validation Error',
                level=logging.WARNING,
                extras=extras
            )
        return response
