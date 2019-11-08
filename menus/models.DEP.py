# TRASH

	#family_id = models.IntegerField(  	# Dep
	#		default=0,
	#	)

# 8 nov
#import datetime

	#def clean_items_by_family(self, family): 
	#	print()
	#	print('Clean Items by Family')
	#	print(family)

		#items = menu.dishes.through.objects.all()
	#	items = menu.items.through.objects.all()

		#items = menu.dishes.through.objects.filter(family=family)
	#	print(items)

		#i = self.dishes.get(title='Causa')
	#	i = self.items.get(title='Causa')
	#	print(i)

		#query_set = m.dishes.filter(family=1)
	#	query_set = m.items.filter(family=1)
	#	print(query_set)



	#get_date():
	#	now = timezone.now()
	#	#return self.pub_date >= timezone.now() - datetime.timedelta(days=7)
	#	return	timezone.now() - datetime.timedelta(days=7) <= self.pub_date <= now






# 6 nov
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)




class Family(models.Model):

	class Meta:
		verbose_name = 'Familia'
		verbose_name_plural = 'Familias'

	name = models.CharField(
		'nombre',
		max_length=100,
		blank=True
	)

	def __str__(self):
		return self.name



class Item(models.Model):

	class Meta:
		ordering = ('family',)
		verbose_name = 'Plato'
		verbose_name_plural = 'Platos'

	name = models.CharField(
		'nombre',
		max_length=200,
		blank=True
	)

	price = models.FloatField(default=0)

	def __str__(self): 
		return self.name


	def get_family():
		pass
	    #return Family.objects.get(id=1)
	    #return Family.objects.get(name='x').id
		#return Family.objects.get(name=False).id

	family = models.ForeignKey(
		Family, 
		on_delete=models.PROTECT,
		blank=True
	)












# 5 nov
	#entries = models.ManyToManyField(items.models.Entry, blank=True)

	#main_courses = models.ManyToManyField(items.models.MainCourse, blank=True)

	#desserts = models.ManyToManyField(items.models.Dessert, blank=True)

	#drinks = models.ManyToManyField(items.models.Drink, blank=True)

	#hot_drinks = models.ManyToManyField(items.models.HotDrink, blank=True)






# 4 nov 
	#entries = models.ManyToManyField(Entry, blank=True)
	#main_courses = models.ManyToManyField(MainCourse, blank=True)
	#desserts = models.ManyToManyField(Dessert, blank=True)
	#drinks = models.ManyToManyField(Drink, blank=True)
	#hot_drinks = models.ManyToManyField(HotDrink, blank=True)


	def entries_empty(self):
		if self.entries.count() == 0:
			return True
		else:
			return False

	def main_courses_empty(self):
		if self.main_courses.count() == 0:
			return True
		else:
			return False

	def desserts_empty(self):
		if self.desserts.count() == 0:
			empty = True
		else:
			empty = False
		return empty


	def drinks_empty(self):
		if self.drinks.count() == 0:
			empty = True
		else:
			empty = False
		return empty

	def hot_drinks_empty(self):
		if self.hot_entries.count() == 0:
			return True
		else:
			return False





		choices=(	
					#('entry', _("Entrada")),
					#('main_course', _("Plato Principal")),
					('entry', "Entrada"),
					('main_course', "Plato Principal"),
					('dessert', "Postre"),
					('drink', "Bebida"),
					('hot_drink', "Bebida Caliente"),
					('spirit_drink', "Bebida Alcholica"),
				),





	#items = models.ManyToManyField(Item)

	#item_0 = models.ForeignKey(
	#	Item, 
	#	on_delete=models.PROTECT,
	#	default=""
	#)


	#menu = models.ForeignKey(
	#	Menu, 
	#	on_delete=models.CASCADE
	#)

	#menus = models.ManyToManyField(Menu)
