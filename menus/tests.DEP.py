


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


