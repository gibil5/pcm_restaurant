"""
Families - Tests

Tests:
	- Views:
"""

from django.test import TestCase
from django.test import Client

#from django.utils import timezone
#from django.urls import reverse

from items.models import Family


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
		
		# Get Response to /items/
		response = c.post('/families/')
		#print(response)


		# Test1 - Check Status Code - Response OK
		print()
		print('\tFamilies - Check Status Code')
		self.assertEqual(response.status_code, 200)


		print()
		print('Test Family 1: End')

