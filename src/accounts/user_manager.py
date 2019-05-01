from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_admin=False, is_staff=False, is_customer=False, is_courier=False,
                    is_merchant=False):
        if not email:
            raise ValueError('Users must have an email address.')
        if not password:
            raise ValueError('Users must have a password.')
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.customer = is_customer
        user_obj.courier = is_courier
        user_obj.merchant = is_merchant
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password=None):
        super_user_obj = self.create_user(
            email,
            password=password,
            is_admin=True,
            is_staff=True
        )
        return super_user_obj

    def create_staffuser(self, email, password=None):
        staff_user_obj = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return staff_user_obj

    def create_customeruser(self, email, password=None):
        customer_user_obj = self.create_user(
            email,
            password=password,
            is_customer=True
        )
        return customer_user_obj

    def create_courieruser(self, email, password=None):
        courier_user_obj = self.create_user(
            email,
            password=password,
            is_courier=True
        )
        return courier_user_obj

    def create_merchantuser(self, email, password=None):
        merchant_user_obj = self.create_user(
            email,
            password=password,
            is_merchant=True
        )
        return merchant_user_obj
