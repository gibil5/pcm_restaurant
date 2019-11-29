"""
Menus - Views
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django import forms
from django.forms import modelform_factory, modelformset_factory

#from . import lib
from .models import *

# Create your views here.



# ------------------------------------------------ Form ---------------------
class DeleteMenuForm(forms.Form):
	pass
	#your_name = forms.CharField(label='Your name', max_length=100)


class MenuForm(forms.ModelForm):

	class Meta:

		model = Menu

		fields = [
					'name',
					'date',
					'family',
					'items',
				]

	name = forms.CharField(max_length=100, label='Nombre')	
	date = forms.DateField(required=False, label='Fecha')
	items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple, label='Platos')



# New Form
class NewMenuForm(forms.ModelForm):

	class Meta:

		model = Menu

		fields = [
					'name',
					'date',
				]



# ------------------------------------------------ Menus ---------------------

def index(request):
	
	#latest_menu_list = Menu.objects.all()
	latest_menu_list = Menu.objects.filter(active=True)
	
	#print(latest_menu_list)

	err_msg = "No existe ningún Menú todavía."

	ctx = {
			'latest_menu_list': latest_menu_list,
			'err_msg': err_msg,
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
		items = menu.items.filter(family=fam.id)

		#items_dic[fam.name] = items
		items_dic[fam] = items


	ctx = {
			'menu': menu,
			'items_dic': items_dic,
			}

	return	render(request, 'menus/menu.html', ctx)




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
		#form = lib.MenuForm(instance=menu, initial={'family': family.name,})


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








def update(request, menu_id):
	print()
	print('update Menu')

	menu = get_object_or_404(Menu, pk=menu_id)

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewMenuForm(request.POST)

		# check whether it's valid:
		if form.is_valid():
			
			form_instance = NewMenuForm(request.POST, instance=menu)

			form_instance.save()

			#return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
			#return HttpResponseRedirect('/menus/')
			return HttpResponseRedirect('/thanks/')



	# Create a blank form
	else:

		# Form from a Model
		form = NewMenuForm(instance=menu)

		form.fields['name'].label = "Nombre"

		# Context
		ctx = {
				'menu': menu,
				'form': form,
			}

		output = render(request, 'menus/edit.html', ctx)

		return HttpResponse(output)







def delete(request, menu_id):
	print()
	print('Delete Menu')
	print(request)
	print(menu_id)

	menu = get_object_or_404(Menu, pk=menu_id)


	# Create and populate
	if request.method == 'POST':
		print('mark')

		form = DeleteMenuForm(request.POST)

		if form.is_valid():

			# process the data in form.cleaned_data as required


			menu.delete()					# Delete !!!


			return HttpResponseRedirect('/thanks/')



	else:

		form = DeleteMenuForm()

		ctx = {
				'menu': menu,
				'form': form,
		}
		output = render(request, 'menus/delete.html', ctx)
		return HttpResponse(output)











def add_item_form(request):
	print()
	print('Add Item Form')
	print(request)


	# Create and populate
	if request.method == 'POST':
		print('mark')
		#pass
		
		# create a form instance and populate it with data from the request:
		form = MenuForm(request.POST)

		#print(form)
		#print()

		print(form.data)
		print()

		name = form.data['name']

		family_name = form.data['family']
		print(name)
		print(family_name)


		menu = Menu.objects.filter(name=name)[0]
		print(menu)

		family = Family.objects.filter(name=family_name)[0]
		print(family)


		# Clean Items - only that family
		qset = menu.items.filter(family=family.id)
		print(qset)

		for iq in qset:
			menu.items.remove(iq)

		print()
		print(menu.items)
		print()
		print()



		# check whether it's valid:
		if form.is_valid():

			# process the data in form.cleaned_data as required
		
			items = form.cleaned_data['items']

			for item in items:
				menu.items.add(item)

			return HttpResponseRedirect('/thanks/')


	# redirect to a new URL:
	return HttpResponseRedirect('/thanks/')







# Add Menu
def add(request):
	print()
	print('Menu - Add')
	print()

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewMenuForm(request.POST)

		# check whether it's valid:
		if form.is_valid():

			print(form.cleaned_data)

			form_instance = NewMenuForm(request.POST)
			print(form_instance)

			new_menu = form_instance.save()


			return HttpResponseRedirect('/thanks/')



	# Create a blank form
	else:

		menu = Menu()
		#print(menu)

		# Form from a Model
		#form = MenuForm()
		#form = MenuForm(instance=menu)
		form = NewMenuForm(instance=menu)

		form.fields['name'].label = "Nombre"


		# Context
		ctx = {
				#'menu': menu,
				'form': form,
			}

		output = render(request, 'menus/add.html', ctx)

		return HttpResponse(output)



def thanks(request):
	print()
	print('Thanks')
	
	ctx = {}
	
	output = render(request, 'menus/thanks.html', ctx)
	
	return HttpResponse(output)




# ------------------------------------------------ Home ---------------------
def home(request):
	ctx = {
		}
	output = render(request, 'menus/home.html', ctx)
	return HttpResponse(output)
