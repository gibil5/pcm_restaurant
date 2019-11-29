"""
Items - Tests

Tests:
	- Views:
"""

from django.test import TestCase
from django.test import Client

#from django.utils import timezone
#from django.urls import reverse

from .models import Item, Family


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
		
		# Get Response to /items/
		response = c.post('/items/')
		#print(response)

		# Test1 - Check Status Code - Response OK
		print()
		print('\tItems - Check Status Code')
		self.assertEqual(response.status_code, 200)



		# Get Response to /families/
		#response = c.post('/families/')
		#print(response)

		# Test1 - Check Status Code - Response OK
		#print()
		#print('\tFamilies - Check Status Code')
		#self.assertEqual(response.status_code, 200)



		print()
		print('Test Item 1: End')
