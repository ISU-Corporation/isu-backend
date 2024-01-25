from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='EDU',
        default_version='v1',
        description='EDU',
        contact=openapi.Contact(email='office@itcodegroup.ru'),
    )
)

urlpatterns = [
    path('', RedirectView.as_view(url='/backend/swagger')),
    path('backend/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('backend/admin/', admin.site.urls),
    path('backend/', include('core.urls')),
    path('backend/auth/', include('djoser.urls')),
    re_path(r'backend/auth/', include('djoser.urls.authtoken')),
]
