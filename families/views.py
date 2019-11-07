from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms



# Create your views here.

from items.models import *


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




# New Form
class NewFamilyForm(forms.ModelForm):

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


