from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms


from .models import *

# Create your views here.


# New Form
class NewTableForm(forms.ModelForm):

	class Meta:

		model = Table

		fields = [
					'name',
					'active',
					'description',
				]

		widgets = {          
			'description': forms.Textarea(attrs={'rows':1, 'cols':100}),  
		}

class DeleteForm(forms.Form):
	pass


# ------------------------------------------------ Tables ---------------------

# Index
def index(request):
	print()
	print('Tables')

	title = 'Mesas'

	objs = Table.objects.all()

	err_msg = "No existe ningún Mesa todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'tables/index.html', ctx)

	return HttpResponse(output)



# Table
def table(request, table_id):

	obj = get_object_or_404(Table, pk=table_id)  	# Get Object

	ctx = {
			'obj': obj,
			}

	return	render(request, 'tables/table.html', ctx)





def add(request):
	print()
	print('Add table')

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewTableForm(request.POST)

		if form.is_valid():

			form_instance = NewTableForm(request.POST)

			new_table = form_instance.save()

			return HttpResponseRedirect('/tables/thanks/')

	# Create a blank form
	else:

		table = Table()

		form = NewTableForm(instance=table)

		ctx = {
				'form': form,
			}

		output = render(request, 'tables/add.html', ctx)

		return HttpResponse(output)








def delete(request, table_id):
	print()
	print('Delete Table')


	obj = get_object_or_404(Table, pk=table_id)


	# Create and populate
	if request.method == 'POST':
		print('mark')

		form = DeleteForm(request.POST)

		if form.is_valid():

			obj.delete()					# Delete !!!

			return HttpResponseRedirect('/tables/thanks/')



	# Create delete form
	else:

		form = DeleteForm()

		ctx = {
				'obj': obj,
				'form': form,
		}
		output = render(request, 'tables/delete.html', ctx)
		return HttpResponse(output)




# Update
def update(request, table_id):
	print()
	print('update Table')


	obj = get_object_or_404(Table, pk=table_id)


	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewTableForm(request.POST)

		# check whether it's valid:
		if form.is_valid():
			
			form_instance = NewTableForm(request.POST, instance=obj)

			form_instance.save()

			return HttpResponseRedirect('/tables/thanks/')


	# Create a blank form
	else:

		# Form from a Model
		form = NewTableForm(instance=obj)

		# Context
		ctx = {
				'obj': obj,
				'form': form,
			}

		output = render(request, 'tables/edit.html', ctx)

		return HttpResponse(output)



def table_thanks(request):
	print()
	print('Tables Thanks')
	ctx = {}
	output = render(request, 'tables/thanks.html', ctx)
	return HttpResponse(output)


