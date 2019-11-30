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

from . import lib_tst

# Create your tests here.




# Test Menu Views Index - Empty
class MenuEmptyTests(lib_tst.ModelEmptyTests):

	def setUp(self):
		print()
		print('setup - MenuEmptyTests')
		
		self.name = 'MenuEmptyTests'

		self.path_index = '/menus/'

		self.msg_error_index_empty = "No existe ningún Menú todavía."

		self.ctx_0_name = "menus"


	def __str__(self):
		return self.name







# Test Menu Views Index - Empty
class MenuIndexTests(lib_tst.ModelIndexTests):

	def setUp(self):
		print()
		print('setup - MenuIndexTests')

		self.path_index = 'menus'

		self.menu_name = '7 Nov 2019'
		self.menu_date = timezone.now()


		self.ctx_0_name = 'menus'

		self.ctx_0_value = '<Menu: 7 Nov 2019>'

		self.debug = False


	# Convenience method
	def create_obj(self):

		return Menu.objects.create(name=self.menu_name, date=self.menu_date)














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

