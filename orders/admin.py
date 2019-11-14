from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Order)



class OrderLineAdmin(admin.ModelAdmin):
	print()

	#fieldsets = [
	#				(None, 		{'fields': ['name'] }),
	#				('order', 	{'fields': ['order'] }),
	#				('items', 	{'fields': ['items'] }),
	#				('qty', 	{'fields': ['qty'] }),
	#			]


	list_display = ['name', 'order', 'item', 'qty']

	list_filter = ['order']


#admin.site.register(OrderLine)
admin.site.register(OrderLine, OrderLineAdmin)


