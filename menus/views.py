"""
Menus - Views

Created:	Oct 2019
Last up:	1 Dec 2019
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

# Index
def index(request):
	print()
	print('* Menu - Index')
	
	# Init
	menus = Menu.objects.filter(active=True)
	
	err_msg = "No existe ningún Menú todavía."

	ctx = {
			'menus': menus,
			'err_msg': err_msg,
		}

	output = render(request, 'menus/menus.html', ctx)

	return HttpResponse(output)



# Detail
def detail(request, menu_id):
	print()
	print('* Menu - Detail')

	# Init
	menu = get_object_or_404(Menu, pk=menu_id)  		# Shortcut !


	# Items Dictionary, by Family
	items_dic = {}

	families = Family.objects.all()

	for fam in families:
		items = menu.items.filter(family=fam.id)
		items_dic[fam] = items


	ctx = {
			'menu': menu,
			'items_dic': items_dic,
			}

	return	render(request, 'menus/menu.html', ctx)




# Update
def update(request, menu_id):
	print()
	print('* Menu - Update')

	# Init
	menu = get_object_or_404(Menu, pk=menu_id)


	# Create object and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewMenuForm(request.POST)

		if form.is_valid():
			
			form_instance = NewMenuForm(request.POST, instance=menu)

			form_instance.save()

			return HttpResponseRedirect('/thanks/')


	# Create a blank form
	else:
		print('* Create a blank form')

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







# Delete
def delete(request, menu_id):
	print()
	print('* Menu - Delete')


	# Init
	menu = get_object_or_404(Menu, pk=menu_id)


	# Create and populate
	if request.method == 'POST':
		print('* Create and populate')

		form = DeleteMenuForm(request.POST)

		if form.is_valid():

			# process the data in form.cleaned_data as required

			menu.delete()					# Delete !!!

			return HttpResponseRedirect('/thanks/')

	# Create a blank form
	else:
		print('* Create a blank form')

		form = DeleteMenuForm()

		ctx = {
				'menu': menu,
				'form': form,
		}
		
		output = render(request, 'menus/delete.html', ctx)
		
		return HttpResponse(output)




# Add
def add(request):
	print()
	print('* Menu - Add')


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
		print('* Create a blank form')

		# Form from a Model
		menu = Menu()
		form = NewMenuForm(instance=menu)
		form.fields['name'].label = "Nombre"

		# Context
		ctx = {
				'form': form,
			}

		output = render(request, 'menus/add.html', ctx)

		return HttpResponse(output)



# Add Item
def add_item(request, menu_id, family_id):
	"""
	Used by: menu
	"""
	print()
	print('* Menu - Add Item')


	# Create and populate
	if request.method == 'POST':
		print('* Create and populate 1')
		
		form = MenuForm(request.POST)

		name = form.data['name']

		family_name = form.data['family']

		menu = Menu.objects.filter(name=name)[0]

		family = Family.objects.filter(name=family_name)[0]


		# Clean Items - only that family
		qset = menu.items.filter(family=family.id)

		for iq in qset:
			menu.items.remove(iq)


		# check whether it's valid:
		if form.is_valid():
		
			items = form.cleaned_data['items']

			for item in items:
				menu.items.add(item)

			return HttpResponseRedirect('/thanks/')


	# Create a blank form
	else:
		print('* Create a blank form 1')

		menu = get_object_or_404(Menu, pk=menu_id)

		family = get_object_or_404(Family, pk=family_id)

		# Form from a Model
		form = MenuForm(instance=menu, initial={'family': family.name,})
		form.fields["items"].queryset = Item.objects.filter(family=family_id)  				# Limit to the family
		form.fields['name'].label = "Nombre"

		ctx = {
				'menu': menu,
				'family': family,
				'form': form,
			}

		output = render(request, 'menus/add_item.html', ctx)

		return HttpResponse(output)



# Thanks
def thanks(request):
	print()
	print('* Menu - Thanks')
	
	ctx = {}
	
	output = render(request, 'menus/thanks.html', ctx)
	
	return HttpResponse(output)


