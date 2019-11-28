from django.contrib import admin

# Register your models here.


from .models import *




class OrderLineAdmin(admin.ModelAdmin):
	print()

	list_display = ['name', 'state', 'item', 'qty', 'total', ]

	list_display_links = ('name',)

	list_filter = ['order']

	#list_editable = ('active',)

	#search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')

	#list_per_page = 25



class OrderAdmin(admin.ModelAdmin):
	print()

	list_display = ['name', 'date', 'state', 'total',  'table', 'waiter', 'cook', 'active']

	list_display_links = ('name', 'date')

	#list_filter = ['order']

	list_editable = ('active',)

	#search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')

	#list_per_page = 25



admin.site.register(OrderLine, OrderLineAdmin)

admin.site.register(Order, OrderAdmin)

