"""
Lines - Views
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

# Create your views here.

from orders.models import *



# New Form
class NewOrderLineForm(forms.ModelForm):

	class Meta:

		model = OrderLine

		fields = [
					#'name',
					'order',
					'item',
					'qty',
				]

	#items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple, label='Platos')


class DeleteForm(forms.Form):
	pass



# ------------------------------------------------ OrderLineLineLines ---------------------

# Index
def index_order(request, order_id):
	print()
	print('OrderLine')

	order = get_object_or_404(Order, pk=order_id)  		# Get Object

	#title = 'Líneas'
	title = order


	#objs = OrderLine.objects.all()
	objs = OrderLine.objects.filter(order=order_id)


	err_msg = "No existe ningún Linea todavía."


	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
			'order': order,
		}

	output = render(request, 'lines/index.html', ctx)

	return HttpResponse(output)




# Index
def index(request):
	print()
	print('OrderLine')

	title = 'Líneas'

	objs = OrderLine.objects.all()

	err_msg = "No existe ningún Linea todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'lines/index.html', ctx)

	return HttpResponse(output)





# OrderLineLine
def line(request, line_id):
	print()
	print('OrderLine')

	obj = get_object_or_404(OrderLine, pk=line_id)  		# Get Object
	
	#lines = OrderLine.objects.filter(line=line_id)

	ctx = {
			'obj': obj,
			#'lines':	lines,
		}

	return	render(request, 'lines/line.html', ctx)





def add_line_order(request, order_id):
	print()
	print('Add line Order')

	order = get_object_or_404(Order, pk=order_id)


	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewOrderLineForm(request.POST)

		if form.is_valid():
			print('Is Valid')

			form_instance = NewOrderLineForm(request.POST)

			new_line = form_instance.save()
			print(new_line)

			#return HttpResponseRedirect('/lines/thanks/')
			return HttpResponseRedirect('/orders/thanks/')


	# Create a blank form
	else:

		line = OrderLine()

		line.order = order


		form = NewOrderLineForm(instance=line)

		ctx = {
				'form': form,
				'order': order,
			}

		#output = render(request, 'lines/add.html', ctx)
		output = render(request, 'lines/add_line_order.html', ctx)

		return HttpResponse(output)






def add(request):
	print()
	print('Add line')

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewOrderLineForm(request.POST)

		if form.is_valid():

			form_instance = NewOrderLineForm(request.POST)

			new_line = form_instance.save()

			return HttpResponseRedirect('/lines/thanks/')


	# Create a blank form
	else:

		line = OrderLine()

		form = NewOrderLineForm(instance=line)

		ctx = {
				'form': form,
			}

		output = render(request, 'lines/add.html', ctx)

		return HttpResponse(output)








def delete(request, line_id):
	print()
	print('Delete OrderLine')


	obj = get_object_or_404(OrderLine, pk=line_id)


	# Create and populate
	if request.method == 'POST':
		print('mark')

		form = DeleteForm(request.POST)

		if form.is_valid():

			obj.delete()					# Delete !!!

			return HttpResponseRedirect('/lines/thanks/')



	# Create delete form
	else:

		form = DeleteForm()

		ctx = {
				'obj': obj,
				'form': form,
		}
		output = render(request, 'lines/delete.html', ctx)
		return HttpResponse(output)




# Update
def update(request, line_id):
	print()
	print('update OrderLine')


	obj = get_object_or_404(OrderLine, pk=line_id)


	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewOrderLineForm(request.POST)

		# check whether it's valid:
		if form.is_valid():
			
			form_instance = NewOrderLineForm(request.POST, instance=obj)

			form_instance.save()

			return HttpResponseRedirect('/lines/thanks/')


	# Create a blank form
	else:

		# Form from a Model
		form = NewOrderLineForm(instance=obj)

		# Context
		ctx = {
				'obj': obj,
				'form': form,
			}

		output = render(request, 'lines/edit.html', ctx)

		return HttpResponse(output)



def line_thanks(request):
	print()
	print('OrderLines Thanks')
	ctx = {}
	output = render(request, 'lines/thanks.html', ctx)
	return HttpResponse(output)


