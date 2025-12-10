import os
from django.contrib import admin
from django.urls import path, include

# Dynamically determine base URL for API endpoints
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    BASE_API_URL = f"https://{codespace_name}-8000.app.github.dev/api/"
else:
    BASE_API_URL = "http://localhost:8000/api/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tracker.urls')),
]
