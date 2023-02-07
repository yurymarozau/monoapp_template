from django.conf import settings
from django.urls import include, path

from api import views
from api.docs import urlpatterns as docs_urlpatterns
from api.v1 import urls as v1_urls

app_name = 'api'

urlpatterns = [
    path('v1/', include(v1_urls.urlpatterns)),
    path('health-check/', views.HealthCheck.as_view()),
    path('', views.ApiInfo.as_view()),
]

if settings.ENABLE_DOCS:
    urlpatterns += [path('docs/', include(docs_urlpatterns))]
