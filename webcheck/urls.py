from django.contrib import admin
from django.urls import path, include
SCRIPT_PREFIX = getattr(settings, 'FORCE_SCRIPT_NAME', None) or ''
urlpatterns = [
    path(f'{SCRIPT_PREFIX.lstrip("/")}/admin/', admin.site.urls),
    path(f'{SCRIPT_PREFIX.lstrip("/")}/', include('webapp.urls')),
]
