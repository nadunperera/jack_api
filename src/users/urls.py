from django.urls import include, path
from rest_framework import routers
from .views import UserProfileViewSet, AddressViewSet, CourierProfileViewSet


router = routers.DefaultRouter()
router.register('user_profiles', UserProfileViewSet)
router.register('addresses', AddressViewSet)
router.register('courier_profiles', CourierProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
