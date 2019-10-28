from django.db import models

# Create your models here.


class Menu(models.Model):


	menu_title = models.CharField(max_length=200)

	date = models.DateTimeField('date')


	def __str__(self): 
		return self.menu_title


