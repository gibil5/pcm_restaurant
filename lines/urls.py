"""
Orders - Urls
"""

from django.urls import path
from . import views


urlpatterns = [

	path('', views.index, name='lines'),
	
	path('<int:line_id>', views.line, name='line'),

	path('add', views.add, name='add_line'),

	path('delete/<int:line_id>', views.delete, name='delete_line'),

	path('update/<int:line_id>', views.update, name='update_line'),

	path('thanks/', views.line_thanks, name='thanks_line'),
]