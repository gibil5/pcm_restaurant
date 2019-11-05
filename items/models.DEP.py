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


