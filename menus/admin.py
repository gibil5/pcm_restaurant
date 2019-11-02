from django.contrib import admin

# Register your models here.


from .models import *


class ItemInline(admin.StackedInline):

	extra = 3

	#model = Item
	#model = Item.tags.through
	model = Menu.dishes.through



class MenuAdmin(admin.ModelAdmin):
	print()

	fieldsets = [
					(None, 					{'fields': ['title'] }),
					('Date Information', 	{'fields': ['date'] }),
				]

	inlines = [ItemInline]

	list_display = ['title', 'date',]




#class ProfileAdmin(MenuAdmin):
#    filter_horizontal = ('opetest',)


admin.site.register(Menu)
#admin.site.register(Menu, MenuAdmin)


#admin.site.register(MainCourse)

#admin.site.register(Dessert)

#admin.site.register(Entry)

#admin.site.register(Drink)

#admin.site.register(HotDrink)
