from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Profile, Address, Courier

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(Courier)

# Remove group model from admin as we are not using it.
admin.site.unregister(Group)
