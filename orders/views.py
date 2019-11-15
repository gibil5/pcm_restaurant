"""
Orders - Views
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

from .models import *

# Create your views here.


# New Form
class NewOrderForm(forms.ModelForm):

	class Meta:

		model = Order

		fields = [
					'date',
					'active',
					'table',
					'waiter',
					'cook',
					#'items',
				]

	#items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple, label='Platos')


class DeleteForm(forms.Form):
	pass


# ------------------------------------------------ Orders ---------------------

# Index
def index(request):
	print()
	print('Orders')

	title = 'Pedidos'

	objs = Order.objects.all()

	err_msg = "No existe ningún Pedido todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'orders/index.html', ctx)

	return HttpResponse(output)






# Order
def order(request, order_id):
	print()
	print('Order')

	obj = get_object_or_404(Order, pk=order_id)  		# Get Object
	
	lines = OrderLine.objects.filter(order=order_id)

	ctx = {
			'obj': obj,
			'lines':	lines,
		}

	return	render(request, 'orders/order.html', ctx)





def add(request):
	print()
	print('Add order')

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewOrderForm(request.POST)

		if form.is_valid():

			form_instance = NewOrderForm(request.POST)

			new_order = form_instance.save()

			return HttpResponseRedirect('/orders/thanks/')


	# Create a blank form
	else:

		order = Order()

		form = NewOrderForm(instance=order)

		ctx = {
				'form': form,
			}

		output = render(request, 'orders/add.html', ctx)

		return HttpResponse(output)








def delete(request, order_id):
	print()
	print('Delete Order')


	obj = get_object_or_404(Order, pk=order_id)


	# Create and populate
	if request.method == 'POST':
		print('mark')

		form = DeleteForm(request.POST)

		if form.is_valid():

			obj.delete()					# Delete !!!

			return HttpResponseRedirect('/orders/thanks/')



	# Create delete form
	else:

		form = DeleteForm()

		ctx = {
				'obj': obj,
				'form': form,
		}
		output = render(request, 'orders/delete.html', ctx)
		return HttpResponse(output)




# Update
def update(request, order_id):
	print()
	print('update Order')


	obj = get_object_or_404(Order, pk=order_id)


	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewOrderForm(request.POST)

		# check whether it's valid:
		if form.is_valid():
			
			form_instance = NewOrderForm(request.POST, instance=obj)

			form_instance.save()

			return HttpResponseRedirect('/orders/thanks/')


	# Create a blank form
	else:

		# Form from a Model
		form = NewOrderForm(instance=obj)

		# Context
		ctx = {
				'obj': obj,
				'form': form,
			}

		output = render(request, 'orders/edit.html', ctx)

		return HttpResponse(output)



def order_thanks(request):
	print()
	print('Orders Thanks')
	ctx = {}
	output = render(request, 'orders/thanks.html', ctx)
	return HttpResponse(output)


