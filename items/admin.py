from django.contrib import admin

# Register your models here.

from .models import *



class FamilyAdmin(admin.ModelAdmin):

	list_display = ('name', 'short_name', 'idx', 'active',)

	list_display_links = ('name', 'short_name')

	#list_filter = ('realtor',)

	#list_editable = ('is_published',)

	#search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')

	#list_per_page = 25



class ItemAdmin(admin.ModelAdmin):

	list_display = ('name', 'family', 'price', 'active',)

	list_display_links = ('name', )

	list_filter = ('family',)

	#list_editable = ('is_published',)

	search_fields = ('name', 'family', 'price',)

	#list_per_page = 25






#admin.site.register(Item)
admin.site.register(Item, ItemAdmin)

#admin.site.register(Family)
admin.site.register(Family, FamilyAdmin)
