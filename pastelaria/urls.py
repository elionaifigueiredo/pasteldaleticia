from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pastel.urls')),
    
]
#libera acesso a pasta images pelo navegador para ser visualizada
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

