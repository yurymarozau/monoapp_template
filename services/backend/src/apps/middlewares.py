from urllib.parse import parse_qs

import jwt
from channels.db import database_sync_to_async
from django.conf import LazySettings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework.exceptions import AuthenticationFailed

settings = LazySettings()
User = get_user_model()


class JWTAuthMiddleware:
    """
    Token authorization middleware for Django Channels 2
    see:
    https://channels.readthedocs.io/en/latest/topics/authentication.html#custom-authentication
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        return JWTAuthMiddlewareInstance(scope, self)


class JWTAuthMiddlewareInstance:
    def __init__(self, scope, middleware):
        self.middleware = middleware
        self.scope = dict(scope)
        self.inner = self.middleware.inner

    async def __call__(self, receive, send):
        query_string = self.scope['query_string']
        if query_string:
            try:
                parsed_query = parse_qs(query_string)
                token_key = parsed_query[b'token'][0].decode()
                user_jwt = jwt.decode(
                    token_key,
                    settings.SECRET_KEY,
                )
                user = await self.get_user(user_jwt['user_id'])
                self.scope['user'] = user
            except (
                AuthenticationFailed,
                jwt.InvalidSignatureError,
                jwt.ExpiredSignatureError,
                jwt.DecodeError,
                KeyError
            ):
                self.scope['user'] = AnonymousUser()
        else:
            self.scope['user'] = AnonymousUser()
        inner = self.inner(self.scope)
        return await inner(receive, send)

    @database_sync_to_async
    def get_user(self, user_uuid):
        try:
            return User.objects.get(uuid=user_uuid)
        except User.DoesNotExist:
            return AnonymousUser()
