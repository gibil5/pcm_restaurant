"""
Orders - Urls
"""

from django.urls import path
from . import views


urlpatterns = [

	path('', views.index, name='orders'),
	
	path('<int:order_id>', views.order, name='order'),

	path('add', views.add, name='add_order'),

	path('delete/<int:order_id>', views.delete, name='delete_order'),

	path('update/<int:order_id>', views.update, name='update_order'),

	path('thanks/', views.order_thanks, name='thanks_order'),
]
