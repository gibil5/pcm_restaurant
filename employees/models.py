from django.db import models

# Create your models here.



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


	def __str__(self): 
		return self.name

