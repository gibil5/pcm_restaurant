"""

Items (Platos)

"""
from django.urls import path
from . import views


urlpatterns = [

	path('', views.items, name='items'),

	path('<int:item_id>', views.item, name='item'),

	path('add', views.add, name='add_item'),

	path('delete/<int:item_id>', views.delete, name='delete_item'),

	path('update/<int:item_id>', views.update, name='update_item'),

	path('thanks/', views.item_thanks, name='thanks_item'),
]
