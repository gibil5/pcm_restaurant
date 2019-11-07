from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

# Create your views here.

from .models import *
from . import lib



# ------------------------------------------------ Classes ---------------------

# New Form
class NewItemForm(forms.ModelForm):
	#print()
	#print('NewItemForm')

	class Meta:

		model = Item

		fields = [
					'name',
					'family',
				]

class DeleteItemForm(forms.Form):
	pass




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





def add(request):
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

		output = render(request, 'items/add.html', ctx)

		return HttpResponse(output)








def delete(request, item_id):
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
		output = render(request, 'items/delete.html', ctx)
		return HttpResponse(output)





def update(request, item_id):
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





def item_thanks(request):
	print()
	print('Items Thanks')
	ctx = {}
	output = render(request, 'items/thanks.html', ctx)
	return HttpResponse(output)
