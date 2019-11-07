from django.urls import path

from . import views

# Anything that has listing/ should look at this file

urlpatterns = [


	path('add_item', views.add_item, name='add_item'),



	#path('items', views.index, name='items'),
	#path('', views.index, name='items'),
	path('', views.items, name='items'),

	#path('<int:item_id>', views.detail, name='item'),
	path('<int:item_id>', views.item, name='item'),



	path('families', views.families, name='families'),
	path('add_family', views.add_family, name='add_family'),

    #path('family/', include('items.urls')),



	path('family//<int:family_id>', views.family, name='family'),

	path('delete_family/<int:family_id>', views.delete_family, name='delete_family'),




	#path('about', views.about, name='about'),



	#path('search', views.search, name='search'),
]
