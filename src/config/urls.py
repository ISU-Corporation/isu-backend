from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from src.config.yasg import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='swagger/')),
]

urlpatterns += swagger_urls
