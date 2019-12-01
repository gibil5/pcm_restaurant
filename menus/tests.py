"""
Menus - Tests

Created: 	29 Nov 2019
Last up: 	 1 Dec 2019

Tests:
	- Views:
		- Index
		- Detail
		- Update

	- Models:
		- Menu
"""

from django.test import TestCase
from django.test import Client

from django.utils import timezone
from django.urls import reverse
from .models import Menu

from . import lib

from . import lib_tst

# Create your tests here.




# ------------------------------------ ModelEmptyTests -----------------------------------------

# Test Menu Views Index - Empty
class MenuEmptyTests(lib_tst.ModelEmptyTests):

	def setUp(self):
		print()
		print('setup - MenuEmptyTests')
		
		self.name = 'MenuEmptyTests'

		self.path_index = '/menus/'

		self.msg_error_index_empty = "No existe ningún Menú todavía."

		self.ctx_0_name = "menus"


	def __str__(self):
		return self.name



# ------------------------------------ ModelIndexTests -----------------------------------------

# Test Menu Views Index - One
class MenuIndexTests(lib_tst.ModelIndexTests):

	def setUp(self):
		print()
		print('setup - MenuIndexTests')

		self.path_index = 'menus'

		self.menu_name = '7 Nov 2019'

		self.menu_date = timezone.now()


		self.ctx_0_name = 'menus'

		self.ctx_0_value = '<Menu: 7 Nov 2019>'

		self.debug = False


	# Convenience method
	def create_obj(self):

		return Menu.objects.create(name=self.menu_name, date=self.menu_date)




# ------------------------------------ ModelDetailTests -----------------------------------------

# Test Menu Views Detail - One
class MenuDetailTests(lib_tst.ModelDetailTests):

	def setUp(self):
		print()
		print('setup - MenuDetailTests')

		self.path_index = '/menus/'

		self.menu_name = '7 Nov 2019'

		self.menu_date = timezone.now()


	# Convenience method
	def create_obj(self):

		return Menu.objects.create(name=self.menu_name, date=self.menu_date)




# ------------------------------------ ModelUpdateTests -----------------------------------------

class MenuUpdateTests(lib_tst.ModelUpdateTests):

	def setUp(self):
		print()
		print('setup - MenuUpdateTests')

		self.path_index = '/menus/update/'

		self.menu_name = '7 Nov 2019'

		self.menu_date = timezone.now()

		self.page_title = 'Modificar'


	# Convenience method
	def create_obj(self):

		return Menu.objects.create(name=self.menu_name, date=self.menu_date)




