from django.urls import path

from . import views

# Anything that has listing/ should look at this file

urlpatterns = [

	path('', views.index, name='menus'),


	path('add', views.add, name='add'),


	path('<int:menu_id>', views.detail, name='menu'),

	#path('search', views.search, name='search'),
]
