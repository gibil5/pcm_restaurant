"""
Employees
"""

from django.urls import path
from . import views


urlpatterns = [


	path('', views.index, name='tables'),
	

	path('<int:table_id>', views.table, name='table'),

	path('add', views.add, name='add_table'),

	path('delete/<int:table_id>', views.delete, name='delete_table'),

	path('update/<int:table_id>', views.update, name='update_table'),

	path('thanks/', views.table_thanks, name='thanks_table'),

]
