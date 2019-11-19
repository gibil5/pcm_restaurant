"""
Orders - Models
"""
from django.db import models
from django.utils import timezone
import locale


# Create your models here.

from tables.models import Table 
from employees.models import Employee
from items.models import Item





# ------------------------------------------------ Orders ---------------------
class Order(models.Model):
	"""
	Order
	"""

	class Meta:
		ordering = ('-date',)
		verbose_name = 'Pedido'
		verbose_name_plural = 'Pedidos'


	draft = 'Inicio'
	preparation = 'Preparación'
	served = 'Servido'
	paid = 'Pagado'
	cancel = 'Cancelado'


	STATES = [
			    (draft, 'Inicio'),
			    (preparation, 'En preparacion'),
				(served, 'Servido'),
				(paid, 'Pagado'),
			    (cancel, 'Cancelado'),
			]

	state = models.CharField(
			max_length=100,
			choices=STATES,
			default = draft,
		)




	total = models.DecimalField(
		'total',
		max_digits=6, 
		decimal_places=2,
		default=0,
	)

	@property
	def total(self):

		total = 0

		lines = OrderLine.objects.filter(order=self.id)

		for line in lines:

			total += line.total


		return total





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

		date = timezone.localtime(self.date)


		#locale.setlocale(locale.LC_TIME, '')

		locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

		#time.strptime(date_string, "%a, %d/%m/%Y")

		#se = '-'
		se = '_'
		return ''.join(
			#[self.date,'-', self.table, '-', self.waiter, '-', self.cook]
			#[self.table.name, '-', self.waiter.name, '-', self.cook.name]
			#[str(self.date), '_', self.table.name, '_', self.waiter.name, '_', self.cook.name]
			#[self.date.strftime('%Y-%m-%d %H:%M'), '_', self.table.name, '_', self.waiter.name, '_', self.cook.name]
			#[self.date.strftime('%d/%m/%Y-%H:%M'), '_', self.table.name, '_', self.waiter.name, '_', self.cook.name]
			#[self.date.strftime('%d/%m/%Y-%H:%M'), '_', self.table.name, ]
			#['Mesa ', self.table.name, '-', self.date.strftime('%d/%m/%Y-%H:%M'),  ]
			#['M', self.table.name, se, self.date.strftime('%d %b_%H:%M'),  ]
			#[self.date.strftime('%A %d %b-%H:%M'),]

			#[self.date.strftime('%a %d %b-%H:%M'),]
			[date.strftime('%A %d %b-%H:%M'),]
		
		).title()	



	date = models.DateTimeField(
		'fecha',
		default=timezone.now
	)


	active = models.BooleanField(
		'activo',
		default=True,
	)



	# Table
	table = models.ForeignKey(
		Table, 
		on_delete=models.PROTECT,
		#blank=True
		verbose_name='mesa',
	)


	# Waiter
	waiter = models.ForeignKey(
		Employee, 
		on_delete=models.PROTECT,
		related_name='waiter',
		limit_choices_to={'is_waiter': True},
		verbose_name='mozo',
	)


	# Cook
	cook = models.ForeignKey(
		Employee, 
		on_delete=models.PROTECT,
		related_name='cook',
		limit_choices_to={'is_cook': True},

		verbose_name='cocinero',
		blank=True,
	)



	def get_items(self):
		"""
		Used by Order - Index
		"""
		s = ''		
		items = Item.objects.filter(order=self.id)
		for item in items:
			s += item.name + ', '
		return s





	def get_lines_2(self):

		lines = OrderLine.objects.filter(order=self.id)

		return lines




	def get_lines(self):
		"""
		Used by Order - Index
		"""
		s = ''
		se = ' x '
		#se_li = ', '
		se_li = ' | '
		
		lines = OrderLine.objects.filter(order=self.id)

		for line in lines:
			s += line.item.name + se + str(line.qty) + se_li
		
		return s


	def __str__(self): 
		return self.name






# ------------------------------------------------ Lines ---------------------
class OrderLine(models.Model):
	"""
	Order Line
	"""

	class Meta:
		#ordering = ('-date',)
		verbose_name = 'Línea'
		verbose_name_plural = 'Líneas'


	name = models.CharField(
		max_length=200,
	)

	@property
	def name(self):
		se = '_'
		return ''.join(
			[self.order.name,'-', self.item.name, '-', str(self.qty), ]
		).title()	




	total = models.DecimalField(
		'total',
		max_digits=6, 
		decimal_places=2,
		default=0,
	)

	@property
	def total(self):
		return self.item.price * self.qty








	order = models.ForeignKey(
		Order, 
		on_delete=models.CASCADE,
		verbose_name='pedido',
	)


	item = models.ForeignKey(
		Item, 
		on_delete=models.CASCADE,
		blank=True,
		verbose_name='plato',
	)


	qty = models.PositiveIntegerField(
		'cantidad',
	)


	def __str__(self): 
		return self.name


