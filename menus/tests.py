"""
Menus - Tests

Tests:
	- Views:
		- Menus
		- Menu
	- Models:
		- Menu
"""

from django.test import TestCase
from django.test import Client

from django.utils import timezone
from django.urls import reverse

from .models import Menu

# Create your tests here.


_MSG_ERROR_EMPTY = "No existe ningún Menú todavía."


# Test Menu Views - Index
class MenuViewTest(TestCase):


	# Test 1
	def test_index_empty(self):
		"""
		Test Index View with no Objects
		"""
		print()
		print('Test Menu 1: Begin')

		#print('Index View. No Menus')


		# Create Client 
		c = Client()
		

		# Get Response to /menus/
		response = c.post('/menus/')
		#print(response)


		# Test1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)


		# Test 2 - Check Page Empty Message
		print()
		print('\tCheck Page Empty Message')
		self.assertContains(response, _MSG_ERROR_EMPTY)


		# Test 3 - Check Context
		print()
		print('\tCheck Context')
		#self.assertQuerysetEqual(response.context["latest_menu_list"], [])
		self.assertQuerysetEqual(response.context["menus"], [])


		print()
		print('Test Menu 1: End')



