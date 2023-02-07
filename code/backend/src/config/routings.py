from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from apps.common.middlewares import JWTAuthMiddleware
from ws.routings import websocket_urlpatterns

application = ProtocolTypeRouter({
    'websocket': JWTAuthMiddleware(
        URLRouter(
            [
                path('ws/', URLRouter(websocket_urlpatterns))
            ]
        )
    ),
})
