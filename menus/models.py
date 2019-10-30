from django.db import models

# Create your models here.


class Item(models.Model):

	item_title = models.CharField(max_length=200)

	pub_date = models.DateTimeField('date created')

	price = models.FloatField(default=0)


	#menu = models.ForeignKey(
	#	Menu, 
	#	on_delete=models.CASCADE
	#)

	#menus = models.ManyToManyField(Menu)


	def __str__(self): 
		return self.item_title


class Menu(models.Model):

	menu_title = models.CharField(max_length=200)

	date = models.DateTimeField('date')

	def __str__(self): 
		return self.menu_title


	#items = models.ManyToManyField(Item)

	item_0 = models.ForeignKey(
		Item, 
		on_delete=models.PROTECT,
		default=""
	)




