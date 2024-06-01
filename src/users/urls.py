from django.urls import include, path
from rest_framework.routers import SimpleRouter

from src.users import views

router = SimpleRouter()
router.register('users', views.User, 'users')

urlpatterns = [
    # Djoser + SimpleJWT
    path('', include('djoser.urls.jwt')),
]

urlpatterns += router.urls
