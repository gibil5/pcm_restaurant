"""
Orders - Urls
"""

from django.urls import path
from . import views


urlpatterns = [

	#path('', views.index, name='stories'),
	path('', views.waiters, name='waiters'),
	

	# Waiter 
	path('waiters', views.waiters, name='waiters'),

	path('waiter/<int:waiter_id>', views.waiter, name='waiter'),


	# Cook
	path('cooks', views.cooks, name='cooks'),

	path('cook/<int:cook_id>', views.cook, name='cook'),
]
