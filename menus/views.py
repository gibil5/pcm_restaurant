#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django import forms
from .models import Menu
from items.models import Family, Item
from items import lib

# Create your views here.


FAMILY_ID = 1
GLOBAL_VAR = 'Magic String' #or matrix...


#class MenuForm(forms.ModelForm):
class MenuForm(forms.ModelForm):
	print()
	print('MenuForm')

	class Meta:

		model = Menu

		fields = [
					'title',
					'date',

					'family',
					'family_id',

					'dishes',
				]
	
	title = forms.CharField(max_length=100)
	
	date = forms.DateField(required=False)
	
	family = forms.CharField(max_length=100)

	#family_id = forms.IntegerField()

	dishes = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple)
	#dishes = forms.ModelMultipleChoiceField(queryset=Item.objects.filter(family=1), widget=forms.widgets.CheckboxSelectMultiple)
	#dishes = forms.ModelMultipleChoiceField(queryset=Item.objects.filter(family=family_id), widget=forms.widgets.CheckboxSelectMultiple)




#def add_item(request, menu_id):
def add_item(request, menu_id, family_id):
	print()
	print('Add Item')
	#print(request)
	#print(menu_id)
	#print(family_id)

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



	# Create a blank form
	else:

		menu = get_object_or_404(Menu, pk=menu_id)
		print(menu)

		family = get_object_or_404(Family, pk=family_id)
		print(family)

		items = Item.objects.filter(family=family.id)
		print(items)


		#form = MenuForm(instance=menu)
		#form = MenuForm(instance=menu, family_id=2)
		#form = MenuForm(initial={'title': 'Initial Title'})
		#form = MenuForm(instance=menu, initial={'title': 'Initial Title', 'family': family.name, 'family_id': family_id})
		form = MenuForm(instance=menu, initial={'title': 'Initial Title', 'family': family.name, 'family_id': family_id, 'dishes': items})



		ctx = {
				#'family': family,
				#'items': items,
				'menu': menu,
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
