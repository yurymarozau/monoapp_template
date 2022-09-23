from channels.routing import URLRouter
from django.urls import path

from ws.v1 import routings as v1_routings

websocket_urlpatterns = [
    path('v1/', URLRouter(v1_routings.websocket_urlpatterns))
]
