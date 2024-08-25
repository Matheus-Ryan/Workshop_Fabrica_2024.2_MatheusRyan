from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AutorViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
