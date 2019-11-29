"""
Menus - Tests

Created: 	29 Nov 2019
Last up: 	id

Tests:
	- Views:
		- Index
		- Menu

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
class MenuViewTest(TestCase):


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
	"""
	"""
	#time = timezone.now() + datetime.timedelta(days=days)

	return Menu.objects.create(name=name, date=date)




# Test Menu Views Index - Populated
class MenuIndexViewTests(TestCase):


	# Test 2
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
		create_obj(name, date)




		# Create Client 
		c = Client()

		response = c.get(reverse('menus'))

		#print(response)
		#print(response.status_code)
		#print(response.context['menus'])
		#print(response.content)

		print()
		print('\tCheck Context')
		self.assertQuerysetEqual(
			
			response.context['menus'],
			
			['<Menu: 7 Nov 2019>']
		)


		print('Test Menu 2: End')



