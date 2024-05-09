from django.urls import include, path

urlpatterns = [
    # Djoser + SimpleJWT
    path('', include('djoser.urls.jwt')),
    path('', include('djoser.urls')),
]
