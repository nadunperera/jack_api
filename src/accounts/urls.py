from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, ProfileViewSet, AddressViewSet, CourierViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)
router.register('addresses', AddressViewSet)
router.register('couriers', CourierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
