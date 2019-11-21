"""

Menus

"""

from django.urls import path
from . import views


urlpatterns = [


	path('', views.index, name='menus'),
	path('home', views.home, name='home'),


	path('menus', views.index, name='menus'),

	#path('menus_today', views.menus_today, name='menus_today'),


	path('<int:menu_id>', views.detail, name='menu'),

	path('add', views.add, name='add_menu'),
	
	path('delete/<int:menu_id>', views.delete, name='delete_menu'),

	path('update/<int:menu_id>', views.update, name='update_menu'),

	path('thanks/', views.thanks, name='thanks_menu'),


	
	# Add item into menu
	path('add_item/<int:menu_id>/<int:family_id>', views.add_item, name='add_item'),

	path('add_item_form/', views.add_item_form, name='add_item_form'),
]
