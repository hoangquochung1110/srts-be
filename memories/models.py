from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

USER_MODEL = get_user_model()

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, blank=False)
    comment = models.TextField(max_length=300, blank=True)
    lat = models.DecimalField(max_digits=11, decimal_places=7, blank=False, null=False)
    long = models.DecimalField(max_digits=11, decimal_places=7, blank=False, null=False)
    creation_date = models.DateTimeField()
    last_modified = models.DateTimeField()
    users = models.ManyToManyField(USER_MODEL, related_name='locations')

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = timezone.now()

        self.last_modified = timezone.now()
        return super(Location, self).save(*args, **kwargs)
