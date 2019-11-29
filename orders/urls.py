"""
Orders - Urls
"""

from django.urls import path
from . import views


urlpatterns = [

	path('', views.index, name='orders'),

	#path('', views.orders_today, name='orders'),


	path('orders_today', views.orders_today, name='orders_today'),
	
	path('sales', views.sales, name='order_sales'),



	# Lines
	path('lines/<int:order_id>', views.order_lines, name='order_lines'),

	path('add_line_order/<int:order_id>', views.add_line_order, name='order_add_line'),





	path('<int:order_id>', views.order, name='order'),

	path('order_cook/<int:order_id>', views.order_cook, name='order_cook'),

	path('order_waiter/<int:order_id>', views.order_waiter, name='order_waiter'),



	


	path('add', views.add, name='add_order'),

	#path('add_order/<int:employee_id>', views.add_order, name='add_order_cook'),




	path('delete/<int:order_id>', views.delete, name='delete_order'),

	path('update/<int:order_id>', views.update, name='update_order'),

	path('thanks/', views.order_thanks, name='thanks_order'),
]
