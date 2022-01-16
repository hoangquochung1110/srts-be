from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, blank=False)
    comment = models.TextField(max_length=300, blank=True)
    lat = models.DecimalField(max_digits=11, decimal_places=7, blank=False, null=False)
    long = models.DecimalField(max_digits=11, decimal_places=7, blank=False, null=False)
    users = models.ManyToManyField(USER_MODEL, related_name='location')
