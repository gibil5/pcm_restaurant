from django.db import models
from django.template.defaulttags import register

# Create your models here.



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




	image = models.CharField(
		'imágen',
		max_length=200,
		blank=True
	)



	notes_cook = models.TextField(
			'notas cocinero',
			blank=True
		)

	notes_waiter = models.TextField(
			'notas mozo',
			blank=True
		)




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

