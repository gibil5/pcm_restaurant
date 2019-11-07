from django.urls import path

from . import views

urlpatterns = [

	path('', views.families, name='families'),

	path('family//<int:family_id>', views.family, name='family'),


	#path('add_family', views.add_family, name='add_family'),
	#path('delete_family/<int:family_id>', views.delete_family, name='delete_family'),
	#path('update_family/<int:family_id>', views.update_family, name='update_family'),

	path('add', views.add, name='add'),
	path('delete/<int:family_id>', views.delete, name='delete'),
	path('update/<int:family_id>', views.update, name='update'),



	path('thanks/', views.family_thanks, name='family_thanks'),

]
