"""
Library Tests Cases

Created: 	30 Nov 2019
Last up: 	id

Used by:
	- Menu
	- Family

In progress...
	- Item 
	- Employee
	- Order
	- OrderLine


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

from django.urls import reverse

from django.utils import timezone


# ------------------------------------ ModelEmptyTests -----------------------------------------

# Test Model Empty Tests
class ModelEmptyTests(TestCase):


	def setUp(self):
		print()
		print('setup - ModelEmptyTests')
		
		self.name = 'ModelEmptyTests'
		
		#self.client = Client()  # Django's TestCase already sets self.client so this line isn't required
		#self.login_status = self.createUserAndLogin(user_name, password)




	# Test 1
	def test_index_empty(self):
		"""
		Test Index View with no Objects
		"""
		print()
		print('\ttest_index_empty : Begin')

		#print(self.name)


		# Create Client 
		c = Client()
		


		# Get Response to /menus/
		response = c.post(self.path_index)
		#print(response)



		# Test1 - Check Status Code - Response OK
		#print()
		#print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)



		# Test 2 - Check Page Empty Message
		#print()
		#print('\tCheck Page Empty Message')
		self.assertContains(response, self.msg_error_index_empty)



		# Test 3 - Check Context - menus
		#print()
		#print('\tCheck Context')
		self.assertQuerysetEqual(response.context[self.ctx_0_name], [])


		print()
		print('\ttest_index_empty: End')




# ------------------------------------ ModelIndexTests -----------------------------------------

# Test Model Views - Index
class ModelIndexTests(TestCase):


	# Test - Index
	def test_index_view_with_a_menu(self):
		"""
		Test Index View with One Object
		"""
		print()
		print('\ttest_index_with_an_obj : Begin')


		# Create Obj
		obj = self.create_obj()


		# Create Client 
		c = Client()

		response = c.get(reverse(self.path_index))

		# Debug
		if self.debug:
			print(response)
			print(response.status_code)
			print(response.context[self.ctx_0_name])
			print(response.content)



		# Test 1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)


		# Test 2 - Check Context - Menus
		print()
		print('\tCheck Context')
		self.assertQuerysetEqual(
			
			response.context[self.ctx_0_name],
			
			[self.ctx_0_value]
		)



		print('\ttest_index_with_an_obj : End')



