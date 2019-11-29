"""
Tests - Urls
"""

from django.urls import path
from . import views


urlpatterns = [

	path('', views.tests, name='tests'),


	#path('clean_orders', views.clean_orders, name='clean_orders'),
	path('clean_orders', views.delete_orders, name='clean_orders'),

	path('create_orders', views.create_orders, name='create_orders'),
]
