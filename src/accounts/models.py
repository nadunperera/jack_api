from django.contrib.auth.models import AbstractBaseUser
from .user_manager import UserManager
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    confirm_email = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)  # superuser
    staff = models.BooleanField(default=False)  # staff
    customer = models.BooleanField(default=False)
    courier = models.BooleanField(default=False)
    merchant = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    # USERNAME_FIELD and password required by default
    REQUIRED_FIELDS = []  # python manage.py createsuperuser

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_customer(self):
        return self.customer

    @property
    def is_courier(self):
        return self.courier

    @property
    def is_merchant(self):
        return self.merchant


class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, unique=True)
    rating = models.SmallIntegerField(null=True, blank=True)
    picture = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.user.email
