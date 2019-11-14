from django.contrib.postgres.fields import ArrayField
	#item_char_arr = ArrayField(
	#		models.CharField(
	#			max_length=10, 
	#			blank=True),
    #       	size=8,
    #  )


    # Items - Array
	item_arr = ArrayField(
			Item,
      	),

