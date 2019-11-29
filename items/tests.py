"""
Items - Tests

Created: 	29 Nov 2019
Last up: 	id

Tests:
	- Views:
		- Index
"""

from django.test import TestCase
from django.test import Client

#from django.utils import timezone
#from django.urls import reverse

from .models import Item, Family

from menus import lib


# Create your tests here.


# Test Menu Views - Index
class ItemViewTest(TestCase):


	# Test 1
	#def test_index_view_with_no_menus(self):
	def test_index_empty(self):
		"""
		Test Index View with no Objects
		"""
		print()
		print('Test Item 1: Begin')


		# Create Client 
		c = Client()

		path = 'items'
		
		lib.test_status_code_ok(self, c, path)



		print()
		print('Test Item 1: End')
