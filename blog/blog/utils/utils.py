import re

from django.conf import settings
from django.conf.urls import url
from django.views.static import serve


def get_settings(key):
    if hasattr(settings, key):
        return getattr(settings, key)
    raise RuntimeError('Empty value for the setting')


def get_static_urls():
    is_debug = get_settings('DEBUG')
    is_serve_media = get_settings('SERVE_MEDIA')
    if not (is_debug or is_serve_media):
        return []

    prefix = get_settings('STATIC_URL')
    root = get_settings('STATIC_ROOT')
    pattern = r'^{}(?P<path>.*)$'.format(re.escape(prefix.lstrip('/')))
    return [url(pattern, serve, kwargs={'document_root': root})]