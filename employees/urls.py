"""

Employees

"""

from django.urls import path
from . import views


urlpatterns = [

	path('', views.employees, name='employees'),

	path('<int:employee_id>', views.employee, name='employee'),

	path('add', views.add, name='add_employee'),

	path('delete/<int:employee_id>', views.delete, name='delete_employee'),

	path('update/<int:employee_id>', views.update, name='update_employee'),

	path('thanks/', views.employee_thanks, name='thanks_employee'),

]
