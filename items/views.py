from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

# Create your views here.

from .models import *
from . import lib




# ------------------------------------------------ Family ---------------------

class DeleteFamilyForm(forms.Form):
	pass


def delete_family(request, family_id):
	print()
	print('Delete family')
	print(request)
	print(family_id)

	family = get_object_or_404(Family, pk=family_id)


	# Create and populate
	if request.method == 'POST':
		print('mark')

		form = DeleteFamilyForm(request.POST)

		if form.is_valid():

			# process the data in form.cleaned_data as required


			family.delete()					# Delete !!!

			return HttpResponseRedirect('/thanks/')


	else:

		form = DeleteFamilyForm()

		ctx = {
				'family': family,
				'form': form,
		}
		output = render(request, 'items/delete_family.html', ctx)
		return HttpResponse(output)





def family(request, menu_id):
	print()
	print('Menu - Family')
	print()

	family = get_object_or_404(Menu, pk=menu_id)  		# Shortcut !
	print(family)


	ctx = {
			'family': family,
			}

	return	render(request, 'items/family.html', ctx)


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



# New Form
class NewFamilyForm(forms.ModelForm):
	print()
	print('NewFamilyForm')

	class Meta:

		model = Family

		fields = [
					'name',

					#'date',
				]

# Add Menu
def add_family(request):
	print()
	print('Family - Add')
	print()



	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewFamilyForm(request.POST)

		# check whether it's valid:
		if form.is_valid():

			print(form.cleaned_data)

			form_instance = NewFamilyForm(request.POST)
			print(form_instance)

			new_family = form_instance.save()


			return HttpResponseRedirect('/thanks/')



	# Create a blank form
	else:

		family = Family()
		#print(menu)

		# Form from a Model
		form = NewFamilyForm(instance=family)

		#form.fields['name'].label = "Nombre"


		# Context
		ctx = {
				'form': form,
			}

		output = render(request, 'items/add_family.html', ctx)

		return HttpResponse(output)







# ------------------------------------------------ Item ---------------------

#def index(request):
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



#def detail(request, item_id):
def item(request, item_id):
	
	item = get_object_or_404(Item, pk=item_id)  	# Get Object

	ctx = {'item': item,}

	return	render(request, 'items/item.html', ctx)


