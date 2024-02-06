from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()

router.register('passcard', views.PassCard, basename='passcard')

urlpatterns = [
    path('user_profile/<int:pk>/', views.UserProfile.as_view(), name='user_profile'),
    path('', include(router.urls))
]
