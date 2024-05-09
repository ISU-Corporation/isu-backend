from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger
    path('', RedirectView.as_view(url='api/schema/swagger-ui/')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Djoser + SimpleJWT
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
]
