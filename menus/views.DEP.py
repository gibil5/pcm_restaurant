# 7 nov

def add_item(request, menu_id, family_id):
	print()
	print('Add Item')


	# Create and populate
	if request.method == 'POST':
		
		# create a form instance and populate it with data from the request:)
		form = MenuForm(request.POST)


		# check whether it's valid:
		if form.is_valid():

			print(form.cleaned_data)

			# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')


	# Create a blank form
	else:

		menu = get_object_or_404(Menu, pk=menu_id)
		#print(menu)

		family = get_object_or_404(Family, pk=family_id)
		print(family)


		# Form from a Model
		form = MenuForm(instance=menu, initial={'family': family.name,})


		# Limit to the family
		form.fields["items"].queryset = Item.objects.filter(family=family_id)

		form.fields['name'].label = "Nombre"


		ctx = {
				'menu': menu,
				'menu_id': menu.id,
				'form': form,
			}

		output = render(request, 'menus/add_item.html', ctx)

		return HttpResponse(output)





# 5 nov

FAMILY_ID = 1
GLOBAL_VAR = 'Magic String' #or matrix...







def add(request):

	menu = Menu()

	ctx = {
			'menu': menu,
			}
	output = render(request, 'menus/add.html', ctx)
	return HttpResponse(output)





		#menu.dishes.through.objects.all().delete()
		#menu.dishes.filter(family=family.id).delete()
		#menu.dishes.filter(family=family.id).clear()
		#menu.clean_items_by_family(family)








# 4 nov 
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
