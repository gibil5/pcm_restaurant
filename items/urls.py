from django.urls import path

from . import views

# Anything that has listing/ should look at this file

urlpatterns = [

	path('items', views.index, name='items'),

	path('about', views.about, name='about'),

	path('<int:item_id>', views.detail, name='item'),


	#path('search', views.search, name='search'),
]
