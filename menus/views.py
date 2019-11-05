#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

#from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect


from django import forms


from .models import Menu
from items.models import Family, Item
from items import lib



from django.forms import modelform_factory, modelformset_factory



# Create your views here.


FAMILY_ID = 1
GLOBAL_VAR = 'Magic String' #or matrix...


#class MenuForm(forms.ModelForm):
class MenuForm(forms.ModelForm):
	print()
	print('MenuForm')

	def __init__(self, *args, **kwargs):
		print('MF - Init')
		
		super().__init__(*args, **kwargs)

		#self.dishes = forms.ModelMultipleChoiceField(queryset=Item.objects.filter(family=1), widget=forms.widgets.CheckboxSelectMultiple)
		#self.dishes = False


	class Meta:

		model = Menu

		fields = [
					'title',
					'date',

					#'family',
					#'family_id',

					'dishes',
				]
	
	title = forms.CharField(max_length=100)
	
	date = forms.DateField(required=False)
	
	#family = forms.CharField(max_length=100)

	#family_id = forms.IntegerField()

	dishes = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple)
	#dishes = forms.ModelMultipleChoiceField(queryset=Item.objects.filter(family=1), widget=forms.widgets.CheckboxSelectMultiple)
	#dishes = forms.ModelMultipleChoiceField(queryset=Item.objects.filter(family=family_id), widget=forms.widgets.CheckboxSelectMultiple)




def thanks(request):

	ctx = {
			}

	output = render(request, 'menus/thanks.html', ctx)
	return HttpResponse(output)



def add_item_form(request):
	print()
	print('Add Item Form')
	print(request)

	#return HttpResponseRedirect('/thanks/')

	# Create and populate
	if request.method == 'POST':
		print('mark')
		#pass
		
		# create a form instance and populate it with data from the request:
		#form = NameForm(request.POST)
		form = MenuForm(request.POST)
		#print(form)

		title = 'Viernes 1 Nov'

		menu = Menu.objects.filter(title=title)[0]
		print(menu)
		menu.dishes.through.objects.all().delete()


		# check whether it's valid:
		if form.is_valid():
		#if True:

			print('mark 2')

			# process the data in form.cleaned_data as required
			# ...
		
			#print(form.data)

			print(form.cleaned_data)

			title = form.cleaned_data['title']
			print(title)


			items = form.cleaned_data['dishes']

			# Remove all
			menu.dishes.through.objects.all().delete()
			print(menu.dishes)

			for item in items:
				print('mark 3')
	
				print(item)

				menu.dishes.add(item)

			print(menu.dishes)

			# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')

		#else:
		#	print('mark 4')
		#	menu.dishes.through.objects.all().delete()



	# redirect to a new URL:
	return HttpResponseRedirect('/thanks/')




#def add_item(request, menu_id):
def add_item(request, menu_id, family_id):
	print()
	print('Add Item')


	# Create and populate
	if request.method == 'POST':
		#pass
		
		# create a form instance and populate it with data from the request:
		#form = NameForm(request.POST)
		form = MenuForm(request.POST)


		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
		
			print(form.cleaned_data)

			# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')


	# Create a blank form
	else:

		menu = get_object_or_404(Menu, pk=menu_id)
		#print(menu)


		# Form from a Model
		#form = MenuForm()
		form = MenuForm(instance=menu)

		# Limit to the family
		form.fields["dishes"].queryset = Item.objects.filter(family=family_id)



		ctx = {
				'menu': menu,
				'menu_id': menu.id,
				'form': form,
			}

		output = render(request, 'menus/add_item.html', ctx)

		return HttpResponse(output)





def index(request):
	
	latest_menu_list = Menu.objects.all()
	print(latest_menu_list)

	ctx = {
			'latest_menu_list': latest_menu_list,
			}

	output = render(request, 'menus/menus.html', ctx)

	return HttpResponse(output)




def detail(request, menu_id):
	print()
	print('Menu - Detail')
	print()

	menu = get_object_or_404(Menu, pk=menu_id)  		# Shortcut !
	print(menu)

	#print(menu.entries.all())
	#print(menu.main_courses.all())
	#print(menu.desserts.all())
	#print()


	# Items Dictionary, by Family
	families = Family.objects.all()

	items_dic = {}
	for fam in families:

		#items = menu.objects.all.filter(family=fam.id)
		items = menu.dishes.filter(family=fam.id)

		#items_dic[fam.name] = items
		items_dic[fam] = items


	ctx = {
			'menu': menu,
			'items_dic': items_dic,
			}

	return	render(request, 'menus/menu.html', ctx)









def add(request):

	#menu = Menu.objects.create()		# Creates and saves
	menu = Menu()

	ctx = {
			'menu': menu,
			}
	output = render(request, 'menus/add.html', ctx)
	return HttpResponse(output)
