"""
Library Tests Cases

Created: 	30 Nov 2019
Last up: 	id

Tests:
	- Views:
		- Index
		- Detail
		- Update

	- Models:
		- Menu
"""



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
		#self.assertContains(response, _MSG_ERROR_EMPTY)
		self.assertContains(response, self.msg_error_index_empty)



		# Test 3 - Check Context
		#print()
		#print('\tCheck Context')
		#self.assertQuerysetEqual(response.context["menus"], [])
		self.assertQuerysetEqual(response.context[self.ctx_0_name], [])


		print()
		print('\ttest_index_empty: End')

