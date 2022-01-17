from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateTimeField(read_only=True)
    last_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Location
        fields = [
            'id', 
            'name', 
            'comment', 
            'lat', 
            'long', 
            'creation_date', 
            'last_modified'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        instance = super().create(validated_data)
        instance.users.add(user)
        instance.save()
        return instance
