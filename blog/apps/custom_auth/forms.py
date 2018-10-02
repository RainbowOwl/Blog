import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib.auth import authenticate

from apps.custom_auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'first_name',
                   'last_name', 'is_superuser', 'is_staff',
                   'date_joined', 'last_login')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exits.')
            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect.')
            if not user.is_active:
                raise forms.ValidationError('This user is inactive.')
        return super().clean()

class RegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password',
                                widget=forms.PasswordInput())
    password2 = forms.CharField(label='password(again)',
                                widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Password do not match')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('username can only contain'
                                        'alphanumeric characters and the'
                                        'underscore')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('username is already taken')

