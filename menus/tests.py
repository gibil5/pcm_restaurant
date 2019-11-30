"""
Menus - Tests

Created: 	29 Nov 2019
Last up: 	id

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
from django.utils import timezone
from django.urls import reverse
from .models import Menu
from . import lib

# Create your tests here.


_MSG_ERROR_EMPTY = "No existe ningún Menú todavía."



# Test Menu Views Index - Empty
class MenuEmptyTests(TestCase):


	# Test 1
	def test_index_empty(self):
		"""
		Test Index View with no Objects
		"""
		print()
		print('Test Menu 1: Begin')
		print('Index View. No Menus')


		# Create Client 
		c = Client()
		
		path = 'menus'
		
		lib.test_status_code_ok(self, c, path)



		# Get Response to /menus/
		#response = c.post('/menus/')
		#print(response)



		# Test1 - Check Status Code - Response OK
		#print()
		#print('\tCheck Status Code')
		#self.assertEqual(response.status_code, 200)



		# Test 2 - Check Page Empty Message
		#print()
		#print('\tCheck Page Empty Message')
		#self.assertContains(response, _MSG_ERROR_EMPTY)


		# Test 3 - Check Context
		#print()
		#print('\tCheck Context')
		#self.assertQuerysetEqual(response.context["menus"], [])


		print()
		print('Test Menu 1: End')





# Convenience method
def create_obj(name, date):
	return Menu.objects.create(name=name, date=date)




# Test Menu Views - Populated
#class MenuOneViewTest(TestCase):


# Test Menu Views - Index
class MenuIndexTests(TestCase):



	# Test 2 - Index
	def test_index_view_with_a_menu(self):
		"""
		Test Index View with One Object
		"""
		print()
		print('Test Menu 2: Begin')
		print('Index View. One Menu')


		# Init
		date= timezone.now()
		name = '7 Nov 2019'


		# Create Menu
		menu = create_obj(name, date)


		# Create Client 
		c = Client()

		response = c.get(reverse('menus'))


		# Test1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)



		#print(response)
		#print(response.status_code)
		#print(response.context['menus'])
		#print(response.content)


		# Test2 - Check Context - Menus
		print()
		print('\tCheck Context')
		self.assertQuerysetEqual(
			
			response.context['menus'],
			
			['<Menu: 7 Nov 2019>']
		)




# Test Menu Views - Detail 
class MenuDetailTests(TestCase):

	# Test 3 - Detail
	def test_detail_view_with_a_menu(self):
		"""
		Test Index View with One Object
		"""
		print()
		print('Test Menu 3: Begin')
		print('Detail View. One Menu')


		# Init
		date= timezone.now()
		name = '7 Nov 2019'

		# Create Menu
		menu = create_obj(name, date)



		# Create Client 
		c = Client()

		response = c.post('/menus/' + str(menu.id))


		# Test1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)

		print('Test Menu 3: End')




# Test Menu Views - Update 
class MenuUpdateTests(TestCase):

	# Test 4 - Update
	def test_update_view_with_a_menu(self):
		"""
		Update View with One Object
		"""
		print()
		print('Test Menu 4: Begin')
		print('Update View. One Menu')


		# Init
		date= timezone.now()
		name = '7 Nov 2019'

		# Create Menu
		menu = create_obj(name, date)
		print(menu)


		# Client
		c = Client()

		response = c.get('/menus/update/' + str(menu.id))



		# Assert 1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)



		# Assert 2 - Check Content
		print()
		print('\tCheck Content')
		self.assertContains(response, "Modificar")



		# Assert 3 - Check Context
		print()
		print('\tCheck Context')

		print(response.context['menu'])
		print("<Menu: 7 Nov 2019>")
		#self.assertEqual(response.context['menu'], "<Menu: 7 Nov 2019>")

		#self.assertEqual(response.context['menu'], ["<Menu: 7 Nov 2019>"])
		#['<Menu: 7 Nov 2019>']




        #self.assertEqual(len(response.context['customers']), 5)


		#self.assertQuerysetEqual(
			#response.context['latest_question_list'],			
			#['<Question: Past question.>']
		#	response.context['menu'],			
		#	['<Question: Past question.>']
		#)




		print('Test Menu 4: End')

