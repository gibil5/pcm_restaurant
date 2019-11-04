


class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)


class ItemForm(forms.Form):

	your_name = forms.CharField(label='Your name', max_length=100)
	
	def __init__(self, method, family):
		print('ItemForm - Init')
		print(family)

		items = Item.objects.filter(family=family.id)
		print(items)

		#for item in items:	
		#	line = forms.CharField(label=item.title, max_length=100)


	#return render(request, 'menus/menus.html')

	#latest_menu_list = Menu.objects.order_by('-pub_date')[:5]


	#return render(request, 'menus/menu.html')

#def search(request):
#	return render(request, 'menus/search.html')
