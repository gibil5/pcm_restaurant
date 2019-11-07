"""pcm URL Configuration
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('menus.urls')),

    path('menus/', include('menus.urls')),
    
    path('items/', include('items.urls')),

    path('families/', include('families.urls')),
]
