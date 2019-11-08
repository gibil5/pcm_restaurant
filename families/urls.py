"""

Families

"""

from django.urls import path
from . import views


urlpatterns = [

	path('', views.families, name='families'),

	path('family/<int:family_id>', views.family, name='family'),

	path('add', views.add, name='add_family'),

	path('delete/<int:family_id>', views.delete, name='delete_family'),

	path('update/<int:family_id>', views.update, name='update_family'),

	path('thanks/', views.family_thanks, name='thanks_family'),

]
