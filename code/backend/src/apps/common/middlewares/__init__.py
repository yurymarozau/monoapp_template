from apps.common.middlewares.jwt_auth import JWTAuthMiddleware
from apps.common.middlewares.monitoring_long_time_queries import \
    MonitoringLongTimeQueriesMiddleware
from apps.common.middlewares.trailing_slash_appending import \
    TrailingSlashAppendingMiddleware
from apps.common.middlewares.validation_errors_to_sentry import \
    ValidationErrorsToSentryMiddleware
