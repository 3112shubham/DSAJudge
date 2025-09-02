from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
SCRIPT_PREFIX = getattr(settings, 'FORCE_SCRIPT_NAME', None) or ''
urlpatterns = [
    path(f'{SCRIPT_PREFIX.lstrip("/")}/admin/' if SCRIPT_PREFIX else 'admin/', admin.site.urls),
    path(f'{SCRIPT_PREFIX.lstrip("/")}/' if SCRIPT_PREFIX else '', include('webapp.urls')),
]
