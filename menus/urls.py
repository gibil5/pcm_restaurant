from django.urls import path

from . import views

# Anything that has listing/ should look at this file

urlpatterns = [

	path('', views.index, name='menus'),


	path('add', views.add, name='add'),


	#path('add_item/<int:menu_id>', views.add_item, name='add_item'),
	
	path('add_item/<int:menu_id>/<int:family_id>', views.add_item, name='add_item'),

	path('add_item_all/<int:menu_id>', views.add_item, name='add_item'),



	path('<int:menu_id>', views.detail, name='menu'),

	#path('search', views.search, name='search'),
]
