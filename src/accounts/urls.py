from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, ProfileViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
