from django.urls import path

from . import views

# Anything that has listing/ should look at this file

urlpatterns = [


	path('add_item', views.add_item, name='add_item'),

	path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),

	path('update_item/<int:item_id>', views.update_item, name='update_item'),


	#path('delete_item', views.delete_item, name='delete_item'),




	path('', views.items, name='items'),
	path('<int:item_id>', views.item, name='item'),



	path('families', views.families, name='families'),
	path('add_family', views.add_family, name='add_family'),
	path('family//<int:family_id>', views.family, name='family'),
	path('delete_family/<int:family_id>', views.delete_family, name='delete_family'),

	path('update_family/<int:family_id>', views.update_family, name='update_family'),

	#path('families/thanks/', views.family_thanks, name='family_thanks'),
	path('thanks/', views.family_thanks, name='family_thanks'),


	#path('search', views.search, name='search'),
]
