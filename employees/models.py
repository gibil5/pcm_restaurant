from django.db import models

import datetime

# Create your models here.
#from orders.models import *
#from orders.models import Order
#from tables.models import Table 



class Employee(models.Model):
	"""
	Employee
	"""

	class Meta:

		#ordering = ('name',)
		#ordering = ('category',)
		ordering = ('is_waiter',)

		verbose_name = 'Empleado'
		verbose_name_plural = 'Empleados'


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


	image = models.CharField(
		'imagen',
		max_length=200,
		default='https://res.cloudinary.com/dam0dmleq/image/upload/v1573501278/pcm/empty_black.png'
	)



	# Active
	active = models.BooleanField(
		'activo',
		default=True,
	)


	#category = models.ForeignKey(
	#	Category, 
	#	on_delete=models.PROTECT,
	#	blank=True
	#)



	is_waiter = models.BooleanField(
			'es mozo ?',
			default=False,
		)

	is_cook = models.BooleanField(
			'es cocinero ?',
			default=False,
		)


	def get_nr_open_orders(self):
		print('mark')

		from orders.models import Order

		today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
		today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

		#objs = Order.objects.all()
		#objs = Order.objects.filter(waiter_id=self.id)
		objs = Order.objects.filter(waiter_id=self.id, date__range=(today_min, today_max))


		count = objs.count()
		#ords = orders.models.Order.objects.all()

		#return orders
		return count


	def __str__(self): 
		return self.name

