# 1 Dec 2019

# ------------------------------------ In prog -----------------------------------------

# Convenience method
def create_obj(name, date):

	return Menu.objects.create(name=name, date=date)




# Test Menu Views - Update 
class MenuUpdateTests_d(TestCase):

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








# Test Menu Views - Detail 
class MenuDetailTests_dep(TestCase):

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






# 30 Nov 2019


# Test Menu Views Detail
class MenuDetailViewTests(TestCase):

	# Test 2
	def test_detail_view_with_a_menu(self):
		"""
		Detail View with One Object
		"""
		print()
		print('Test Menu 2: Begin')
		print('Index View. One Menu')


		c = Client()

		response = c.post('/menus/56')

		# Test1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)



# Test Menu Update
class MenuUpdateViewTests(TestCase):

	# Test 2
	def test_update_view_with_a_menu(self):
		"""
		Detail View with One Object
		"""
		print()
		print('Test Menu 2: Begin')
		print('Index View. One Menu')


		c = Client()

		response = c.post('/menus/update/56')

		# Test1 - Check Status Code - Response OK
		print()
		print('\tCheck Status Code')
		self.assertEqual(response.status_code, 200)












# 29 Nov 2019

# Convenience method
def create_question(question_text, date):
	"""
	"""
	#time = timezone.now() + datetime.timedelta(days=days)

	return Menu.objects.create(name=question_text, date=date)




class MenuIndexViewTests(TestCase):


	# Test 2
	def test_index_view_with_a_menu(self):
		"""
		"""
		print()
		print('Test 2: Begin')
		print('Index View. One Menu')


		c = Client()


		date= timezone.now()

		name = '7 Nov 2019'

		create_question(name, date)

		#response = self.client.get(reverse('polls:index'))
		#response = c.get(reverse('menus:index'))
		response = c.get(reverse('menus'))

		print(response)
		print(response.status_code)
		print(response.context['latest_menu_list'])
		#print(response.content)


		self.assertQuerysetEqual(
			response.context['latest_menu_list'],
			['<Menu: 7 Nov 2019>']
		)


		print('Test 2: End')





# Test Menu Views - Detail 
class MenuDetailTests(TestCase):


	# Test 3
	def test_detail_view_with_a_past_menu(self):
		"""
		Menus with a pub_date in the past are displayed on the Index page.
		"""
		print()
		print('Test 3: Begin')
		print('Index View. One Menu')

		c = Client()

		date= timezone.now()

		name = '7 Nov 2019'

		#menu = create_menu(menu_text="Past menu.", days=-5)
		menu = create_question(name, date)

		#response = self.client.get(reverse('polls:detail', args=(past_menu.id,)))
		response = c.get(reverse('menu', args=(menu.id,)))

		print(response)
		print(response.status_code)
		print(response.context['menu'])


		self.assertContains(
			response,
			menu.name,
			status_code=200
		)

		print('Test 3: End')
		print()


