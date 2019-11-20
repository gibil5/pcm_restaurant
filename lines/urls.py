"""
Orders - Urls
"""

from django.urls import path
from . import views


urlpatterns = [

	path('', views.index, name='lines'),
	
	#path('lines/<int:order_id>', views.index_order, name='lines_order'),


	path('<int:line_id>', views.line, name='line'),


	path('add', views.add, name='add_line'),
	#path('add/<int:order_id>', views.add_line_order, name='add_line'),


	#path('add_line_order/<int:order_id>', views.add_line_order, name='add_line_order'),


	path('delete/<int:line_id>', views.delete, name='delete_line'),




	path('update/<int:line_id>', views.update, name='update_line'),

	path('update_line_state_plus/<int:line_id>', views.update_line_state_plus, name='update_line_state_plus'),

	path('update_line_state_minus/<int:line_id>', views.update_line_state_minus, name='update_line_state_minus'),



	#path('update_line_preparation/<int:line_id>', views.update_preparation, name='update_line_preparation'),
	#path('update_line_ready/<int:line_id>', views.update_ready, name='update_line_ready'),
	#path('update_line_served/<int:line_id>', views.update_served, name='update_line_served'),




	path('thanks/', views.line_thanks, name='thanks_line'),
]
