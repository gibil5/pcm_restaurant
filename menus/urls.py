from django.urls import path

from . import views

# Anything that has listing/ should look at this file

urlpatterns = [

	path('', views.index, name='menus'),
	path('<int:menu_id>', views.detail, name='menu'),
	path('thanks/', views.thanks, name='thanks'),


	# Add
	path('add', views.add, name='add'),
	path('add_item_form/', views.add_item_form, name='add_item_form'),
	#path('add_item/<int:menu_id>', views.add_item, name='add_item'),
	path('add_item_all/<int:menu_id>', views.add_item, name='add_item'),
	path('add_item/<int:menu_id>/<int:family_id>', views.add_item, name='add_item'),


	path('delete_menu/<int:menu_id>', views.delete_menu, name='delete_menu'),


	#path('search', views.search, name='search'),
]
