from django.db import models

# Create your models here.


class Family(models.Model):

	name = models.CharField(
		max_length=100,
		#default='x',
		#default=False,
		blank=True
	)

	title = models.CharField(
		max_length=200,
		#default='x',
		#default=False,
		blank=True
	)

	def __str__(self):
		return self.title



class Item(models.Model):

	#item_title = models.CharField(max_length=200)
	#pub_date = models.DateTimeField('date created')


	title = models.CharField(
		max_length=200,
		default=False,
	)

	price = models.FloatField(default=0)


	def __str__(self): 
		return self.item_title



	
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

	def __str__(self):
		return self.title


class Dessert(Item):

	def __str__(self):
		return self.title


class Entry(Item):

	def __str__(self):
		return self.title


#class Drinks(Item):
class Drink(Item):

	def __str__(self):
		return self.title


#class HotDrinks(Item):
class HotDrink(Item):

	def __str__(self):
		return self.title





class Menu(models.Model):

	#menu_title = models.CharField(max_length=200)
	title = models.CharField(max_length=200)

	date = models.DateTimeField('date')

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






