import factory
from .models import Location
import random

class LocationFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Location %s' % n)
    lat = round(random.uniform(0.00, 100.00), 2)
    long = round(random.uniform(0.00, 100.00), 2)

    class Meta:
        model = Location