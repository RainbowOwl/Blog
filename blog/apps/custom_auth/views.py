from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView

from apps.custom_auth.forms import LoginForm, RegistrationForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,
                            password=password)
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:index')

class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def register_page(request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = user.objects.create_user(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password1'],
                                                email=form.cleaned_data['email'])
                return reverse('blog:index')
