from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()

router.register('schedules', views.Schedule, basename='schedules')
router.register('passcard', views.PassCard, basename='passcard')
router.register('subject', views.Subject, basename='subject')
router.register('homework', views.Homework, basename='homework')

urlpatterns = [
    path('user_profile/<int:pk>/', views.UserProfile.as_view(), name='user_profile'),
    path('', include(router.urls))
]
