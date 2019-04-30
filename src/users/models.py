from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    is_customer = models.BooleanField(default=False)
    is_courier = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=10, unique=True)
    rating = models.IntegerField(blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


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
    postcode = models.CharField(max_length=4)
    state = models.CharField(max_length=3, choices=STATE)
    country = models.CharField(max_length=50, default='Australia')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_profile.user.email


class CourierProfile(models.Model):
    drivers_license = models.PositiveSmallIntegerField()
    drivers_license_expiry = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user_profile.user.email
