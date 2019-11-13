from django.db import models

# Create your models here.


class Table(models.Model):
	"""
	Table
	"""

	class Meta:
		ordering = ('name',)
		verbose_name = 'Mesa'
		verbose_name_plural = 'Mesas'


	name = models.CharField(
		'nombre',
		max_length=200,
		blank=True
	)


	description = models.CharField(
		'descripción',
		max_length=200,
		blank=True
	)


	# Active
	active = models.BooleanField(
			default=True,
		)


	def __str__(self): 
		return self.name

