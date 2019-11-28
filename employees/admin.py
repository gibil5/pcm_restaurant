from django.contrib import admin

# Register your models here.

from .models import *

class EmployeeAdmin(admin.ModelAdmin):

	list_display = ('name', 'is_waiter', 'is_cook', 'active',)

	list_display_links = ('name', )

	#list_filter = ('realtor',)

	list_editable = ('active',)

	#search_fields = ('title', 'description', 'address', 'city', 'zipcode', 'price')

	#list_per_page = 25



admin.site.register(Employee, EmployeeAdmin)

