from django.urls import path

from . import views

# Anything that has listing/ should look at this file

urlpatterns = [

	path('', views.index, name='menus'),

	#path('<int:menu_id>', views.menu, name='menu'),
	path('<int:menu_id>', views.detail, name='menu'),


	#path('search', views.search, name='search'),
]
