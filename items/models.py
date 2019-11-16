"""
Items - Models
"""

from django.db import models
from django.template.defaulttags import register

# Create your models here.


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)



class Family(models.Model):
	"""
	Familia
	"""

	class Meta:

		ordering = ('idx',)

		verbose_name = 'Familia'
		verbose_name_plural = 'Familias'


	name = models.CharField(
		'nombre',
		max_length=100,
		blank=True
	)


	idx = models.IntegerField(
		'orden',
		default=0
	)



	# Active
	active = models.BooleanField(
			default=True,
		)




	def __str__(self):
		return self.name




class Item(models.Model):
	"""
	Plato 
	"""

	class Meta:

		#ordering = ('family',)
		ordering = ('family', 'name', )

		verbose_name = 'Plato'
		verbose_name_plural = 'Platos'


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


	#price = models.FloatField(default=0)
	price = models.DecimalField(
		'precio',
		max_digits=6, 
		decimal_places=2
	)



	image = models.CharField(
		'imagen',
		max_length=200,

		#blank=True

		#default='https://res.cloudinary.com/dam0dmleq/image/upload/v1573501282/pcm/empty_mount_2.png'
		default='https://res.cloudinary.com/dam0dmleq/image/upload/v1573501278/pcm/empty_black.png'
	)



	notes_cook = models.TextField(
			'notas cocinero',
			blank=True
		)


	notes_waiter = models.TextField(
			'notas mozo',
			blank=True
		)


	family = models.ForeignKey(
		Family, 
		on_delete=models.PROTECT,
		blank=True,
		verbose_name='familia',
	)



	# Active
	active = models.BooleanField(
			default=True,
		)


	def __str__(self): 
		return self.name


	#def get_family():
	#	pass
	    #return Family.objects.get(id=1)
	    #return Family.objects.get(name='x').id
		#return Family.objects.get(name=False).id


