import logging

import sentry_sdk
from sentry_sdk import Scope


class SentryService:
    def set_extras(self, scope: Scope = None, extras: dict = None) -> None:
        if scope is None or extras is None:
            return
        for extra_key, extra_value in extras.items():
            scope.set_extra(extra_key, extra_value)

    def set_level(self, scope: Scope = None, level: int = logging.INFO) -> None:
        scope.set_level(logging.getLevelName(level).lower())

    def capture_message(
        self,
        message: str = '',
        level: int = logging.INFO,
        extras: dict = None
    ) -> None:
        with sentry_sdk.push_scope() as scope:
            self.set_extras(scope, extras)
            self.set_level(scope, level)
            sentry_sdk.capture_message(message=message)
