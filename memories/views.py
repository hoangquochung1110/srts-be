from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from .serializers import LocationSerializer
from .models import Location

# Create your views here.

class LocationCreateListViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(users=self.request.user.id)