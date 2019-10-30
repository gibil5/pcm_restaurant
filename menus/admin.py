from django.contrib import admin

# Register your models here.


#from .models import Menu, Item
from .models import *





#class FamilyInline(admin.StackedInline):
#	model = Family



#class MainCourseInline(admin.TabularInline):
#class MainCourseInline(admin.TabularInline):
    #pass
    #model = MainCourse.members.through
	#model = MainCourse.quote_set.related.through
	#model = MainCourse.director.through
	#extra = 3
#	model = MainCourse


class MainCourseInline(admin.StackedInline):
	model = MainCourse

class FamilyAdmin(admin.ModelAdmin):
	print()

	inlines = [MainCourseInline]

	list_display = ['title', ]




#class MenuAdmin(admin.ModelAdmin):
#	print()

#	fieldsets = [
#					(None, 					{'fields': ['title'] }),
#					('Fecha', 				{'fields': ['date'] }),
#				]

	#inlines = [FamilyInline]
	#inlines = [MainCourseInline]

#	list_display = ['title', 'date']
	#list_display = ['title', 'Fecha']

#	list_filter = ['date']

	#search_fields = ['question_text']



admin.site.register(Menu)
#admin.site.register(Menu, MenuAdmin)


#admin.site.register(Item)
#admin.site.register(Item, ItemAdmin)


admin.site.register(Family)
#admin.site.register(Family, FamilyAdmin)

admin.site.register(MainCourse)

admin.site.register(Dessert)

admin.site.register(Entry)

admin.site.register(Drink)

admin.site.register(HotDrink)
