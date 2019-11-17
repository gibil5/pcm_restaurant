"""
Orders - Urls
"""

from django.urls import path
from . import views


urlpatterns = [

	path('', views.index, name='stories'),
	
	# Waiter 
	path('waiters', views.waiters, name='waiters'),

	#path('waiter', views.waiter, name='waiter'),
	path('waiter/<int:waiter_id>', views.waiter, name='waiter'),


	# Cook
	path('cooks', views.cooks, name='cooks'),

	path('cook', views.cook, name='cook'),
]
