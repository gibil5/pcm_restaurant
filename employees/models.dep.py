class Category(models.Model):
	"""
	Category
	"""

	class Meta:

		ordering = ('idx',)

		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'


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
