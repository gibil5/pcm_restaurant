from django.urls import path

from . import views

# Anything that has listing/ should look at this file

urlpatterns = [

	path('', views.index, name='menus'),

	path('<int:menu_id>', views.detail, name='menu'),

	path('add', views.add, name='add'),


	#path('delete_menu/<int:menu_id>', views.delete_menu, name='delete_menu'),
	#path('update_menu/<int:menu_id>', views.update_menu, name='update_menu'),

	path('delete/<int:menu_id>', views.delete, name='delete'),
	path('update/<int:menu_id>', views.update, name='update'),


	path('thanks/', views.thanks, name='thanks'),




	# Add
	#path('add_item_form/', views.add_item_form, name='add_item_form'),
	#path('add_item_all/<int:menu_id>', views.add_item, name='add_item'),
	#path('add_item/<int:menu_id>/<int:family_id>', views.add_item, name='add_item'),


	#path('search', views.search, name='search'),
]
