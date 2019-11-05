from django.db import models

from django.utils.translation import gettext as _

import datetime
from django.utils import timezone


# Create your models here.


#from items.models import *

import items.models


class Item(models.Model):
	def get_family():
		pass

class Menu(models.Model):

	class Meta:
		#verbose_name = '1. Menu'
		#verbose_name_plural = '1. Menus'
		verbose_name = 'Menu'
		verbose_name_plural = 'Menus'

	
	title = models.CharField(
		'nombre',
		max_length=200,
	)


	family = models.CharField(
			max_length=200, 
			blank=True,
		)

	family_id = models.IntegerField(
			default=0,
			#blank=True,
		)



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
		return self.title



	# Items
	dishes = models.ManyToManyField(
		items.models.Item, 
		related_name='dishes',
		blank=True,
		)


	#entries = models.ManyToManyField(items.models.Entry, blank=True)

	#main_courses = models.ManyToManyField(items.models.MainCourse, blank=True)

	#desserts = models.ManyToManyField(items.models.Dessert, blank=True)

	#drinks = models.ManyToManyField(items.models.Drink, blank=True)

	#hot_drinks = models.ManyToManyField(items.models.HotDrink, blank=True)



