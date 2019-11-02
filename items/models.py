from django.db import models

from django.template.defaulttags import register

# Create your models here.



@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)



class Family(models.Model):

	class Meta:
		verbose_name = '1. Familia'
		verbose_name_plural = '1. Familias'

	name = models.CharField(
		max_length=100,
		blank=True
	)

	def __str__(self):
		return self.name



class Item(models.Model):

	title = models.CharField(
		max_length=200,
		blank=True
	)

	price = models.FloatField(default=0)

	def __str__(self): 
		return self.title


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




class Entry(Item):

	class Meta:
		verbose_name = '2. Entrada'
		verbose_name_plural = '2. Entradas'


class MainCourse(Item):

	class Meta:
		verbose_name = '3. Plato Principal'
		verbose_name_plural = '3. Platos Principales'


class Dessert(Item):

	class Meta:
		verbose_name = '4. Postre'
		verbose_name_plural = '4. Postres'




class Drink(Item):

	class Meta:
		verbose_name = '5. Bebida'
		verbose_name_plural = '5. Bebidas'


class HotDrink(Item):

	class Meta:
		verbose_name = '6. Bebida Caliente'
		verbose_name_plural = '6. Bebidas Calientes'


