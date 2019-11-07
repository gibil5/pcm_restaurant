from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

# Create your views here.

from .models import *
from . import lib



def family_thanks(request):
	print()
	print('Family Thanks')
	ctx = {}
	output = render(request, 'families/thanks.html', ctx)
	return HttpResponse(output)


# ------------------------------------------------ Families ---------------------

def families(request):
	print()
	print('Families')

	families = Family.objects.all()

	print(families)

	ctx = {
			'families': families,
			}

	output = render(request, 'items/families.html', ctx)

	return HttpResponse(output)


def family(request, menu_id):
	print()
	print('Family')
	print()

	family = get_object_or_404(Menu, pk=menu_id)  		# Shortcut !
	print(family)

	ctx = {
			'family': family,
			}

	return	render(request, 'items/family.html', ctx)






class DeleteFamilyForm(forms.Form):
	pass


def delete_family(request, family_id):
	print()
	print('Delete family')

	family = get_object_or_404(Family, pk=family_id)


	# Create and populate
	if request.method == 'POST':
		print('mark')

		form = DeleteFamilyForm(request.POST)

		if form.is_valid():

			family.delete()					# Delete !!!

			return HttpResponseRedirect('/thanks/')

	# Create delete form
	else:

		form = DeleteFamilyForm()

		ctx = {
				'family': family,
				'form': form,
		}
		output = render(request, 'items/delete_family.html', ctx)
		return HttpResponse(output)





# New Form
class NewFamilyForm(forms.ModelForm):
	print()
	print('NewFamilyForm')

	class Meta:

		model = Family

		fields = [
					'name',
				]

# Add Family
def add_family(request):
	print()
	print('Add Family')

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewFamilyForm(request.POST)

		if form.is_valid():

			form_instance = NewFamilyForm(request.POST)

			new_family = form_instance.save()

			return HttpResponseRedirect('/thanks/')

	# Create a blank form
	else:

		family = Family()

		form = NewFamilyForm(instance=family)

		ctx = {
				'form': form,
			}

		output = render(request, 'items/add_family.html', ctx)

		return HttpResponse(output)




def update_family(request, family_id):
	print()
	print('update Family')

	family = get_object_or_404(Family, pk=family_id)


	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewFamilyForm(request.POST)

		# check whether it's valid:
		if form.is_valid():
			
			form_instance = NewFamilyForm(request.POST, instance=family)

			form_instance.save()

			#return HttpResponseRedirect('/thanks/')
			return HttpResponseRedirect('/families/thanks/')


	# Create a blank form
	else:

		# Form from a Model
		form = NewFamilyForm(instance=family)

		form.fields['name'].label = "Nombre"

		# Context
		ctx = {
				'family': family,
				'form': form,
			}

		output = render(request, 'families/edit.html', ctx)

		return HttpResponse(output)
















# ------------------------------------------------ Items ---------------------

def items(request):
	print()
	print('Items')

	
	# Items Dictionary, by Family
	items_dic = lib.get_items_dic()
	print(items_dic)


	# Items
	item_list = Item.objects.order_by('family')
	#print(item_list)
	
	ctx = {
			'items_dic': items_dic,
			}

	output = render(request, 'items/items.html', ctx)
	#print(output)

	return HttpResponse(output)



def item(request, item_id):
	
	item = get_object_or_404(Item, pk=item_id)  	# Get Object

	ctx = {'item': item,}

	return	render(request, 'items/item.html', ctx)



# New Form
class NewItemForm(forms.ModelForm):
	print()
	print('NewItemForm')

	class Meta:

		model = Item

		fields = [
					'name',
					'family',
				]



def add_item(request):
	print()
	print('Add item')

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewItemForm(request.POST)

		if form.is_valid():

			form_instance = NewItemForm(request.POST)

			new_item = form_instance.save()

			return HttpResponseRedirect('/thanks/')

	# Create a blank form
	else:

		item = Item()

		form = NewItemForm(instance=item)

		ctx = {
				'form': form,
			}

		output = render(request, 'items/add_item.html', ctx)

		return HttpResponse(output)






class DeleteItemForm(forms.Form):
	pass


def delete_item(request, item_id):
	print()
	print('Delete Item')


	item = get_object_or_404(Item, pk=item_id)


	# Create and populate
	if request.method == 'POST':
		print('mark')

		form = DeleteItemForm(request.POST)

		if form.is_valid():

			item.delete()					# Delete !!!

			return HttpResponseRedirect('/thanks/')



	# Create delete form
	else:

		form = DeleteItemForm()

		ctx = {
				'item': item,
				'form': form,
		}
		output = render(request, 'items/delete_item.html', ctx)
		return HttpResponse(output)





def update_item(request, item_id):
	print()
	print('update Item')

	item = get_object_or_404(Item, pk=item_id)


	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewItemForm(request.POST)

		# check whether it's valid:
		if form.is_valid():
			
			form_instance = NewItemForm(request.POST, instance=item)

			form_instance.save()

			#return HttpResponseRedirect('/thanks/')
			return HttpResponseRedirect('/items/thanks/')


	# Create a blank form
	else:

		# Form from a Model
		form = NewItemForm(instance=item)

		form.fields['name'].label = "Nombre"

		# Context
		ctx = {
				'item': item,
				'form': form,
			}

		output = render(request, 'items/edit.html', ctx)

		return HttpResponse(output)





