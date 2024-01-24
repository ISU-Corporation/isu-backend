from django.urls import path
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()


router.register('schedules', views.Schedule, basename='schedules')

urlpatterns = [

]

urlpatterns += router.urls
