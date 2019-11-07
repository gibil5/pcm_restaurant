from django.urls import path

from . import views

# Anything that has listing/ should look at this file

urlpatterns = [

	path('', views.items, name='items'),

	path('<int:item_id>', views.item, name='item'),

	path('add_item', views.add_item, name='add_item'),

	path('delete_item/<int:item_id>', views.delete_item, name='delete_item'),

	path('update_item/<int:item_id>', views.update_item, name='update_item'),


	path('thanks/', views.item_thanks, name='item_thanks'),


	#path('search', views.search, name='search'),
]
