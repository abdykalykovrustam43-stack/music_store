from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app.urls')),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='schema')
    ),
    path('login/', TokenObtainPairView.as_view(), name='login'),

    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]