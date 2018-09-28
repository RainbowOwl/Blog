from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
]
