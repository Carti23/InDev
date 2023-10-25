from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Staking API')


api_urlpatterns = [
    path('authentication/', include('authentication.urls')),
    path('crypto_staking/', include('crypto_staking.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('swagger/', schema_view),
    path('api/base-auth/', include('rest_framework.urls')),
]
