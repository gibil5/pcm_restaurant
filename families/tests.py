"""
Families - Tests

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

from items.models import Family

from menus import lib


# Create your tests here.


# Test Menu Views - Index
class FamilyViewTest(TestCase):


	# Test 1
	def test_index_empty(self):
		"""
		Test Index View with no Objects
		"""
		print()
		print('Test Family 1: Begin')



		# Create Client 
		c = Client()

		path = 'families'
		
		lib.test_status_code_ok(self, c, path)




		print()
		print('Test Family 1: End')

