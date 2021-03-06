# Generated by Django 3.2.11 on 2022-01-16 01:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, max_length=300)),
                ('lat', models.DecimalField(decimal_places=7, max_digits=11)),
                ('long', models.DecimalField(decimal_places=7, max_digits=11)),
                ('users', models.ManyToManyField(related_name='location', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
