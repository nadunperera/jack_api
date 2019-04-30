from django.contrib import admin
from .models import User, UserProfile, Address, CourierProfile

admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(CourierProfile)
