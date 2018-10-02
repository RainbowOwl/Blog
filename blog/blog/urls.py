from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.static import serve
from blog.admin import portfolio_admin_site


from blog.utils.utils import get_static_urls


urlpatterns = [
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('admin/', portfolio_admin_site.urls),
    path('^static/(?P<path>.*)$', serve, kwargs={'document_root': settings.STATIC_ROOT}),
    path('api/', include('api.urls', namespace='api')),
    path('auth/', include('apps.custom_auth.urls', namespace='auth')),

]

urlpatterns = urlpatterns + get_static_urls()
