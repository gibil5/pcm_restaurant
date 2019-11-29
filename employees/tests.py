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

from .models import Employee

from menus import lib


# Create your tests here.


# Test Employee Views - Index
class EmployeeViewTest(TestCase):


	# Test 1
	def test_index_empty(self):
		"""
		Test Index View with no Objects
		"""
		print()
		print('Test Employee 1: Begin')


		# Create Client 
		c = Client()

		path = 'employees'
		
		lib.test_status_code_ok(self, c, path)


		print()
		print('Test Employee 1: End')


