import factory
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Sequence(lambda n: 'user%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)   
    
    class Meta:
        model = USER_MODEL

