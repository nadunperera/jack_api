from rest_framework import serializers
from .models import User, Profile, Address, Courier


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CourierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'
