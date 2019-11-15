"""
Orders - Models
"""
from django.db import models
from django.utils import timezone

# Create your models here.

from tables.models import Table 
from employees.models import Employee
from items.models import Item


class Order(models.Model):
	"""
	Order
	"""

	class Meta:
		#ordering = ('name',)
		verbose_name = 'Pedido'
		verbose_name_plural = 'Pedidos'




	# Items - ManyToMany
	items = models.ManyToManyField(
		Item, 
		blank=True,
	)




	name = models.CharField(
		'nombre',
		max_length=200,
		#blank=True
		)

	@property
	def name(self):
		return ''.join(
			#[self.date,'-', self.table, '-', self.waiter, '-', self.cook]
			#[self.table.name, '-', self.waiter.name, '-', self.cook.name]
			#[str(self.date), '_', self.table.name, '_', self.waiter.name, '_', self.cook.name]
			#[self.date.strftime('%Y-%m-%d %H:%M'), '_', self.table.name, '_', self.waiter.name, '_', self.cook.name]
			#[self.date.strftime('%d/%m/%Y-%H:%M'), '_', self.table.name, '_', self.waiter.name, '_', self.cook.name]
			#[self.date.strftime('%d/%m/%Y-%H:%M'), '_', self.table.name, ]
			#['Mesa ', self.table.name, '-', self.date.strftime('%d/%m/%Y-%H:%M'),  ]
			['Mesa ', self.table.name, '-', self.date.strftime('%d %b-%H:%M'),  ]
		)	



	date = models.DateTimeField(
		'fecha',
		default=timezone.now
	)


	active = models.BooleanField(
			default=True,
		)



	# Table
	table = models.ForeignKey(
		Table, 
		on_delete=models.PROTECT,
		#blank=True
	)


	# Waiter
	waiter = models.ForeignKey(
		Employee, 

		on_delete=models.PROTECT,

		related_name='waiter',

		limit_choices_to={'is_waiter': True},
	)


	# Cook
	cook = models.ForeignKey(
		Employee, 

		on_delete=models.PROTECT,

		related_name='cook',

		limit_choices_to={'is_cook': True},

		blank=True
	)


	def get_items(self):
		s = ''		
		items = Item.objects.filter(order=self.id)
		for item in items:
			s += item.name + ', '
		return s


	def __str__(self): 
		return self.name




class OrderLine(models.Model):
	"""
	Order Line
	"""

	name = models.CharField(
		max_length=200,
	)

	order = models.ForeignKey(
		Order, 
        on_delete=models.CASCADE,
	)


	item = models.ForeignKey(
		Item, 
        on_delete=models.CASCADE,
		blank=True,
	)


	qty = models.IntegerField()


	def __str__(self): 
		return self.name

