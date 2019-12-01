"""
Families - Tests

Created: 	29 Nov 2019
Last up: 	id

Tests:
	- Views Empty:
		- Index

	- Views One:
		- Index
"""

from django.test import TestCase
from django.test import Client

from django.utils import timezone
#from django.urls import reverse

from items.models import Family

from menus import lib, lib_tst


# Create your tests here.


# Test Menu Views - Index
class FamilyEmptyTests(lib_tst.ModelEmptyTests):


	def setUp(self):
		print()
		print('setup - FamilyEmptyTests')
		
		self.name = 'FamilyEmptyTests'

		self.path_index = '/families/'

		self.msg_error_index_empty = "No existe ninguna Familia todavía."

		self.ctx_0_name = "families"




# Test Menu Views Index - Empty
class FamilyIndexTests(lib_tst.ModelIndexTests):

	def setUp(self):
		print()
		print('setup - FamilyIndexTests')

		self.path_index = 'families'

		self.family_name = 'Comida Peruana'

		self.ctx_0_name = 'families'

		self.ctx_0_value = '<Family: Comida Peruana>'

		self.debug = False


	# Convenience method
	def create_obj(self):

		return Family.objects.create(name=self.family_name)



