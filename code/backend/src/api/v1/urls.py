from django.urls import include, path

from api.v1 import auth as auth_urls

app_name = 'v1'

urlpatterns = [
    path('auth/', include(auth_urls.urlpatterns)),
]
