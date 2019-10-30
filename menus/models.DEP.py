		choices=(	
					#('entry', _("Entrada")),
					#('main_course', _("Plato Principal")),
					('entry', "Entrada"),
					('main_course', "Plato Principal"),
					('dessert', "Postre"),
					('drink', "Bebida"),
					('hot_drink', "Bebida Caliente"),
					('spirit_drink', "Bebida Alcholica"),
				),





	#items = models.ManyToManyField(Item)

	#item_0 = models.ForeignKey(
	#	Item, 
	#	on_delete=models.PROTECT,
	#	default=""
	#)


	#menu = models.ForeignKey(
	#	Menu, 
	#	on_delete=models.CASCADE
	#)

	#menus = models.ManyToManyField(Menu)
