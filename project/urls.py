from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from core.views import frontpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')),
    path('', include('store.urls')),
    path('',frontpage,name='frontpage'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
