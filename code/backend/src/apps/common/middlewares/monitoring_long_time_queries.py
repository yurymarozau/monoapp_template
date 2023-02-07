import logging
import time

from django.conf import settings

from apps.common.utils.sentry_service import SentryService


class MonitoringLongTimeQueriesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        request.start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - request.start_time
        if duration > settings.REQUEST_TIME_LOG_THRESHOLD:
            if hasattr(response, 'data'):
                response_data = response.data
            else:
                response_data = response.content
            extras = {
                'GET': request.GET,
                'POST': request.POST,
                'response': response_data,
                'request_duration': '{request_time:.2f} sec'.format(request_time=duration),
            }
            SentryService().capture_message(
                message='API query is longer than {request_time} seconds. ({view})'.format(
                    request_time=settings.REQUEST_TIME_LOG_THRESHOLD,
                    view=request.resolver_match._func_path.rsplit('.', 1)[1]
                ),
                level=logging.WARNING,
                extras=extras
            )
        return response
