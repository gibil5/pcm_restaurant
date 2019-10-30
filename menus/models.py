from django.db import models

from django.utils.translation import gettext as _


# Create your models here.


class Family(models.Model):

	class Meta:
		verbose_name = '2. Familia'
		verbose_name_plural = '2. Familias'


	name = models.CharField(
		max_length=100,
		blank=True
	)


	#title = models.CharField(
	#	max_length=200,
	#	blank=True
	#)


	def __str__(self):
		#return self.title
		return self.name





class Item(models.Model):

	#item_title = models.CharField(max_length=200)
	#pub_date = models.DateTimeField('date created')


	title = models.CharField(
		max_length=200,
		#default=False,
		blank=True
	)

	price = models.FloatField(default=0)


	def __str__(self): 
		return self.title



	
	def get_family():
		pass
	    #return Family.objects.get(id=1)
	    #return Family.objects.get(name='x').id
	#    return Family.objects.get(name=False).id


	family = models.ForeignKey(
		Family, 
		on_delete=models.PROTECT,
		#default=get_family,
		blank=True
	)






class MainCourse(Item):

	class Meta:
		verbose_name = '4. Plato Principal'
		verbose_name_plural = '4. Platos Principales'




class Dessert(Item):

	class Meta:
		verbose_name = '5. Postre'
		verbose_name_plural = '5. Postres'




class Entry(Item):

	class Meta:
		verbose_name = '3. Entrada'
		verbose_name_plural = '3. Entradas'



class Drink(Item):

	class Meta:
		verbose_name = '6. Bebida'
		verbose_name_plural = '6. Bebidas'





class HotDrink(Item):

	class Meta:
		verbose_name = '7. Bebida Caliente'
		verbose_name_plural = '7. Bebidas Calientes'




class Menu(models.Model):

	class Meta:
		verbose_name = '1. Menu'
		verbose_name_plural = '1. Menus'


	#menu_title = models.CharField(max_length=200)
	
	title = models.CharField(
		'nombre',
		max_length=200,
	)


	date = models.DateTimeField(
		#'date',
		'fecha',
	)


	def __str__(self): 
		return self.title


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




	main_courses = models.ManyToManyField(MainCourse, blank=True)


	desserts = models.ManyToManyField(Dessert, blank=True)


	entries = models.ManyToManyField(Entry, blank=True)


	#driks = models.ManyToManyField(Drinks)
	drinks = models.ManyToManyField(Drink, blank=True)

	hot_drinks = models.ManyToManyField(HotDrink, blank=True)






