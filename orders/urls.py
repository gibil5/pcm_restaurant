"""
Orders - Urls
"""

from django.urls import path
from . import views


urlpatterns = [

	path('', views.index, name='orders'),
	
	path('sales', views.sales, name='order_sales'),



	# Lines
	path('lines/<int:order_id>', views.order_lines, name='order_lines'),

	path('add_line_order/<int:order_id>', views.add_line_order, name='order_add_line'),



	path('<int:order_id>', views.order, name='order'),

	path('add', views.add, name='add_order'),

	path('delete/<int:order_id>', views.delete, name='delete_order'),

	path('update/<int:order_id>', views.update, name='update_order'),

	path('thanks/', views.order_thanks, name='thanks_order'),
]
