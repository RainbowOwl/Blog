from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.static import serve

from blog.utils.utils import get_static_urls

urlpatterns = [
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
    path('^static/(?P<path>.*)$', serve, kwargs={'document_root': settings.STATIC_ROOT}),
    path('api/', include('api.urls', namespace='api')),
]

urlpatterns = urlpatterns + get_static_urls()
