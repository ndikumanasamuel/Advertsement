
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('', include('core_advert.urls')),
     # path('admin/', admin.site.urls),
    
]
