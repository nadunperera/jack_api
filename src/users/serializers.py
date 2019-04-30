from rest_framework import serializers
from .models import UserProfile, Address, CourierProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = 'id', 'url', 'user_profile', 'street', 'suburb', 'postcode', 'state', 'country', 'created', 'modified'


class CourierProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourierProfile
        fields = 'id', 'url', 'user_profile', 'drivers_license', 'drivers_license_expiry', 'created', 'modified'
