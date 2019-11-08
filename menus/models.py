from django.db import models
from django.utils.translation import gettext as _
from django.template.defaulttags import register

from django.utils import timezone

# Create your models here.


from items.models import *


class Menu(models.Model):
	"""
	Menu
	"""

	class Meta:

		ordering = ('-date',)

		verbose_name = 'Menu'
		verbose_name_plural = 'Menus'

	
	name = models.CharField(
		verbose_name='nombre',
		max_length=200,
	)


	#date = models.DateTimeField(
	date = models.DateField(
		'fecha',
		default=timezone.now
	)


	family = models.CharField(
			max_length=200, 
			blank=True,
		)


	# Items
	items = models.ManyToManyField(
		Item, 
		blank=True,
	)


	def __str__(self): 
		return self.name








