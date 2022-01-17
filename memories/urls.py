from rest_framework.routers import DefaultRouter
from .views import LocationCreateListViewSet
from django.urls import path, include

router = DefaultRouter()

router.register(r'locations', LocationCreateListViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]