from rest_framework.routers import DefaultRouter
from .views import LocationCreateListViewSet, FacebookLogin
from django.urls import path, include

router = DefaultRouter()

router.register(r'locations', LocationCreateListViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login')
]