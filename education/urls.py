from django.urls import path, include
from rest_framework.routers import DefaultRouter

from education import views

router = DefaultRouter()

router.register('schedules', views.Schedule, basename='schedules')
router.register('subject', views.Subject, basename='subject')
router.register('homework', views.Homework, basename='homework')

urlpatterns = [
    path('', include(router.urls))
]
