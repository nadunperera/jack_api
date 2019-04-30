from .models import UserProfile, Address, CourierProfile
from rest_framework import viewsets
from .serializers import UserProfileSerializer, AddressSerializer, CourierProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CourierProfileViewSet(viewsets.ModelViewSet):
    queryset = CourierProfile.objects.all()
    serializer_class = CourierProfileSerializer
