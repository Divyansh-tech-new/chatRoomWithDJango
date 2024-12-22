from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),  # Include your app's URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development
