import imp
from django.test import TestCase
from memories.factories import LocationFactory
from users.factories import UserFactory
from memories.models import Location
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
import json
from rest_framework import status
from django.urls import reverse

class LocationCreateListViewSetTest(TestCase):
    def setUp(self) -> None:
        self.user1 = UserFactory()
        self.user2 = UserFactory()

        self.locA = LocationFactory()
        self.locA.users.add(self.user1)

        self.locB = LocationFactory()
        self.locB.users.add(self.user1)

        self.client1 = APIClient()
        token = Token.objects.create(user=self.user1)
        self.client1.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.base_url = '/locations/'

    def test_list_location(self):
        location_count = Location.objects.filter(users=self.user1).count()
        response = self.client1.get(self.base_url, format="json")
        jsonized_res = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(location_count, len(jsonized_res))

    def test_create_location(self):
        previous_user1_location_count = Location.objects.filter(users=self.user1).count()
        
        request_data = {
            "name": "Loc X",
            "comment": "com Y",
            "lat": "10.9959550",
            "long": "106.5112710"
        }
        response = self.client1.post(self.base_url, data=request_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        current_user1_location_count = Location.objects.filter(users=self.user1).count()
        self.assertEqual(current_user1_location_count, previous_user1_location_count + 1)