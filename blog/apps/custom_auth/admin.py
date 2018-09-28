from django.contrib import admin

from apps.custom_auth.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'last_login')

    class Meta:
        model = User
