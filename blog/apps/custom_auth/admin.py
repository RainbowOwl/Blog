from django.contrib import admin
from apps.custom_auth.forms import UserForm
from apps.custom_auth.models import User

from apps.custom_auth.models import User
from blog.admin import PorfolioModelAdmin, \
    portfolio_admin_site

class UserAdmin(PorfolioModelAdmin):
    list_display = ('edit_link', 'username',
                    'email', 'role', 'last_login')

    form = UserForm
    model = User

portfolio_admin_site.register(User, UserAdmin)