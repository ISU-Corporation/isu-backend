from django.urls import path
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()


router.register('schedules', views.Schedule, basename='schedules')

urlpatterns = [
    path('user_profile/<int:pk>/', views.UserProfile.as_view(), name='user_profile'),
]

urlpatterns += router.urls
