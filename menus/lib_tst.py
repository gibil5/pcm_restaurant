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




# ------------------------------------ ModelDetailTests -----------------------------------------

# Test Model Views - Detail 
class ModelDetailTests(TestCase):

	# Test 3 - Detail
	def test_detail_view_with_a_menu(self):
		"""
		Test Detail View with One Object
		"""
		print()
		print('\ttest_detail_view_with_a_menu : Begin')


		# Create Obj
		obj = self.create_obj()


		# Create Client 
		c = Client()

		# Get Response
		#response = c.post('/menus/' + str(menu.id))
		response = c.post(self.path_index + str(obj.id))


		# Test1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)


		print()
		print('\ttest_detail_view_with_a_menu : Begin')




# ------------------------------------ ModelUpdateTests -----------------------------------------

# Test Model Views - Update 
class ModelUpdateTests(TestCase):

	# Test 4 - Update
	def test_update_view_with_a_menu(self):
		"""
		Update View with One Object
		"""
		print()
		print('\ttest_update_view_with_a_menu : Begin')



		# Create Obj
		obj = self.create_obj()


		# Client
		c = Client()

		# Get Response
		#response = c.get('/menus/update/' + str(menu.id))
		response = c.get(self.path_index + str(obj.id))



		# Assert 1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)


		# Assert 2 - Check Content
		print()
		print('\tCheck Content')
		#self.assertContains(response, "Modificar")
		self.assertContains(response, self.page_title)


		# Assert 3 - Check Context
		#print()
		#print('\tCheck Context')
		#print(response.context['menu'])
		#print("<Model: 7 Nov 2019>")
		#self.assertEqual(response.context['menu'], "<Model: 7 Nov 2019>")


		print()
		print('\ttest_update_view_with_a_menu : End')





# ------------------------------------ ModelDeleteTests -----------------------------------------

# Test Model Views - Delete 
class ModelDeleteTests(TestCase):


	# Test 4 - Delete
	def test_delete_view_with_a_menu(self):
		"""
		Delete View with One Object
		"""
		print()
		print('\ttest_delete_view_with_a_menu : Begin')



		# Create Obj
		obj = self.create_obj()


		# Client
		c = Client()

		# Get Response
		#response = c.get('/menus/delete/' + str(menu.id))
		response = c.get(self.path_index + str(obj.id))



		# Assert 1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)


		# Assert 2 - Check Content
		print()
		print('\tCheck Content')
		#self.assertContains(response, "Modificar")
		self.assertContains(response, self.page_title)


		# Assert 3 - Check Context
		#print()
		#print('\tCheck Context')
		#print(response.context['menu'])
		#print("<Model: 7 Nov 2019>")
		#self.assertEqual(response.context['menu'], "<Model: 7 Nov 2019>")


		print()
		print('\ttest_delete_view_with_a_menu : End')







# ------------------------------------ ModelAddTests -----------------------------------------

# Test Model Views - Add 
class ModelAddTests(TestCase):


	# Test 4 - Add
	def test_Add_view_with_a_menu(self):
		"""
		Add View with One Object
		"""
		print()
		print('\ttest_add_view_with_a_menu : Begin')



		# Create Obj
		obj = self.create_obj()


		# Client
		c = Client()

		# Get Response
		#response = c.post(self.path_index)		
		#response = c.get('/menus/add')
		response = c.get(self.path_index)



		# Assert 1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)


		# Assert 2 - Check Content
		print()
		print('\tCheck Content')
		#self.assertContains(response, "Modificar")
		self.assertContains(response, self.page_title)


		# Assert 3 - Check Context
		#print()
		#print('\tCheck Context')
		#print(response.context['menu'])
		#print("<Model: 7 Nov 2019>")
		#self.assertEqual(response.context['menu'], "<Model: 7 Nov 2019>")


		print()
		print('\ttest_add_view_with_a_menu : End')





# ------------------------------------ ModelThanksTests -----------------------------------------

# Test Model Views - Thanks 
class ModelThanksTests(TestCase):


	# Test 4 - Thanks
	def test_Thanks_view_with_a_menu(self):
		"""
		Thanks View with One Object
		"""
		print()
		print('\ttest_thanks_view_with_a_menu : Begin')



		# Create Obj
		obj = self.create_obj()


		# Client
		c = Client()

		# Get Response
		#response = c.post(self.path_index)		
		#response = c.get('/menus/thanks')
		response = c.get(self.path_index)



		# Assert 1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		#self.assertEqual(response.status_code, 200)
		self.assertEqual(response.status_code, 301)


		# Assert 2 - Check Content
		#print()
		#print('\tCheck Content')
		#self.assertContains(response, "Modificar")
		#self.assertContains(response, self.page_title)


		# Assert 3 - Check Context
		#print()
		#print('\tCheck Context')
		#print(response.context['menu'])
		#print("<Model: 7 Nov 2019>")
		#self.assertEqual(response.context['menu'], "<Model: 7 Nov 2019>")


		print()
		print('\ttest_thanks_view_with_a_menu : End')





