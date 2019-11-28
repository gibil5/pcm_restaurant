from django.contrib import admin

# Register your models here.

from .models import *


class MenuAdmin(admin.ModelAdmin):

	list_display = ('name', 'date', 'active',)

	list_display_links = ('name',)

	#list_filter = ('realtor',)

	list_editable = ('active',)

	#search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')

	#list_per_page = 25


admin.site.register(Menu, MenuAdmin)
