from django.db import models
from django.utils.translation import gettext as _
import datetime
from django.utils import timezone

# Create your models here.

import items.models



class Menu(models.Model):

	class Meta:
		verbose_name = 'Menu'
		verbose_name_plural = 'Menus'

	

	#title = models.CharField(
	name = models.CharField(
		'nombre',
		max_length=200,
	)



	family = models.CharField(
			max_length=200, 
			blank=True,
		)

	family_id = models.IntegerField(
			default=0,
		)



	def clean_items_by_family(self, family): 
		print()
		print('Clean Items by Family')
		print(family)

		#items = menu.dishes.through.objects.all()
		items = menu.items.through.objects.all()

		#items = menu.dishes.through.objects.filter(family=family)
		print(items)

		#i = self.dishes.get(title='Causa')
		i = self.items.get(title='Causa')
		print(i)

		#query_set = m.dishes.filter(family=1)
		query_set = m.items.filter(family=1)
		print(query_set)



	#get_date():
	#	now = timezone.now()
	#	#return self.pub_date >= timezone.now() - datetime.timedelta(days=7)
	#	return	timezone.now() - datetime.timedelta(days=7) <= self.pub_date <= now


	date = models.DateTimeField(
		#'date',
		'fecha',
		default=datetime.date.today
	)


	def __str__(self): 
		return self.name



	# Items
	#dishes = models.ManyToManyField(
	items = models.ManyToManyField(
		items.models.Item, 
		#related_name='dishes',
		blank=True,
	)





class Item(models.Model):
	def get_family():
		pass



