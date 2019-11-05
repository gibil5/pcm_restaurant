		#family = get_object_or_404(Family, pk=family_id)
		#print(family)

		#items = Item.objects.filter(family=family.id)
		#print(items)


		#FamilyForm = modelform_factory(Family, fields=('name', ))
		#print(FamilyForm)


		#form = MenuForm(instance=menu)
		#form = MenuForm(instance=menu, family_id=2)
		#form = MenuForm(initial={'title': 'Initial Title'})
		#form = MenuForm(instance=menu, initial={'title': 'Initial Title', 'family': family.name, 'family_id': family_id})
		#form = MenuForm(instance=menu, initial={'title': 'Initial Title', 'family': family.name, 'family_id': family_id, 'dishes': items})



		#MenuForm = modelform_factory(
		#								Menu, 
		#								fields=('title', 'date', 'dishes'),
		#								widgets = {
		#											'dishes': forms.widgets.CheckboxSelectMultiple,
		#								},
		#							)

		#MenuForm = modelformset_factory(Menu, fields=('title', 'date', 'dishes'))
		#print(MenuForm)


		#form = FamilyForm()
		#form = MenuForm(instance=menu)
		#formset = MenuForm()
		#print(formset)








def add_item(request, menu_id, family_id):

	# Create and populate
	if request.method == 'POST':
		pass

		# create a form instance and populate it with data from the request:
		#form = NameForm(request.POST)

		# check whether it's valid:
		#if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
		#	return HttpResponseRedirect('/thanks/')





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
