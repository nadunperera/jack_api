from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_courier = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)


class Profile(models.Model):
    contact_number = models.CharField(max_length=10, unique=True)
    rating = models.IntegerField(blank=True)
    picture = models.CharField(max_length=255, blank=True)
    drivers_license = models.CharField(max_length=20, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.email


class Address(models.Model):
    STATE = (
        ('NSW', 'New South Wales'),
        ('VIC', 'Victoria'),
        ('SA', 'South Australia'),
        ('WA', 'Western Australia'),
        ('NT', 'Northern Territory'),
        ('TAS', 'Tasmania'),
    )

    street = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    post_code = models.CharField(max_length=4)
    state = models.CharField(max_length=3, choices=STATE)
    country = models.CharField(max_length=50, default='Australia')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.street
