from django.urls import path

from apps.custom_auth.views import LoginView

app_name = 'custom_auth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]