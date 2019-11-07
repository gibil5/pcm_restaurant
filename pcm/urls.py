"""pcm URL Configuration
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('', include('menus.urls')),

    path('menus/', include('menus.urls')),
    
    path('items/', include('items.urls')),


    #path('families/', include('items.urls')),

    path('families/', include('families.urls')),



    path('admin/', admin.site.urls),
]
