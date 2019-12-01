"""

PCM Restaurant

URL Configuration

"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),


    path('', include('menus.urls')),  			   # Root

    path('menus/', include('menus.urls')),
    
    path('items/', include('items.urls')),

    path('families/', include('families.urls')),

    path('employees/', include('employees.urls')),
    
    path('tables/', include('tables.urls')),
    
    path('orders/', include('orders.urls')),

    path('lines/', include('lines.urls')),

    path('stories/', include('stories.urls')),


    path('tests/', include('tests.urls')),


    path('pages/', include('pages.urls')),
]
