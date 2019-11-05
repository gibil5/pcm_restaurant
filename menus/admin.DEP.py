# 5 nov

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



#admin.site.register(Menu, MenuAdmin)

#admin.site.register(MainCourse)

#admin.site.register(Dessert)

#admin.site.register(Entry)

#admin.site.register(Drink)

#admin.site.register(HotDrink)






# 4 nov 
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

#admin.site.register(Menu, MenuAdmin)


#admin.site.register(Item)
#admin.site.register(Item, ItemAdmin)

