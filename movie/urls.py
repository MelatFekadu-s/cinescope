
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
