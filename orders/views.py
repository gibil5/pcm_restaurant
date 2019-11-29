"""
Views - Orders
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
import datetime
from .models import *

#from . import lib


# Create your views here.


# ------------------------------------------------ Forms ---------------------

# Order
class NewOrderForm(forms.ModelForm):

	class Meta:

		model = Order

		fields = [
					'date',
					'waiter',
					'state',
					'active',
					'table',
					'cook',
				]

	#items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple, label='Platos')


# Order Line
class NewOrderLineForm(forms.ModelForm):

	class Meta:

		model = OrderLine

		fields = [
					'order',
					'item',
					'qty',
					'state',
				]

	#items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple, label='Platos')



# Delete
class DeleteForm(forms.Form):
	pass





# ------------------------------------------------ Orders ---------------------

def orders_today(request):
	
	print()
	print('Orders')

	title = 'Pedidos Hoy'

	today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

	#objs = Order.objects.exclude(state='Pagado')
	#objs = Order.objects.filter(waiter=waiter_id, date__range=(today_min, today_max))
	objs = Order.objects.filter(date__range=(today_min, today_max))



	err_msg = "No existe ningún Pedido todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'orders/index.html', ctx)

	return HttpResponse(output)




# Index
def index(request):
	print()
	print('Orders')

	title = 'Pedidos'

	objs = Order.objects.exclude(state='Pagado')

	err_msg = "No existe ningún Pedido todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'orders/index.html', ctx)

	return HttpResponse(output)




# Index Sales
def sales(request):
	print()
	print('Sales')

	title = 'Ventas'

	#objs = Order.objects.all()
	objs = Order.objects.filter(state='Pagado')

	err_msg = "No existe ninguna Venta todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'orders/index.html', ctx)

	return HttpResponse(output)





# Order Cook
def order_cook(request, order_id):
	print()
	print('Order Cook')

	obj = get_object_or_404(Order, pk=order_id)  		# Get Object
	
	#title = 'Día del Cocinero - ' + obj.name

	lines = OrderLine.objects.filter(order=order_id)

	ctx = {
			#'title': title,
			'obj': obj,
			'lines':	lines,
		}

	return	render(request, 'orders/order_cook.html', ctx)




# Order Cook
def order_waiter(request, order_id):
	print()
	print('Order Waiter')

	obj = get_object_or_404(Order, pk=order_id)  		# Get Object
	
	title = 'Día del Mesero - ' + obj.name

	lines = OrderLine.objects.filter(order=order_id)

	ctx = {
			'title': title,
			'obj': obj,
			'lines':	lines,
		}

	#return	render(request, 'orders/order.html', ctx)
	return	render(request, 'orders/order_waiter.html', ctx)




# Order
def order(request, order_id):
	print()
	print('Order')

	obj = get_object_or_404(Order, pk=order_id)  		# Get Object
	
	title = obj.name
	#title = 'Día del Mesero - ' + obj.name

	lines = OrderLine.objects.filter(order=order_id)

	ctx = {
			'title': title,
			'obj': obj,
			'lines':	lines,
		}

	return	render(request, 'orders/order.html', ctx)



# Add
def add(request):
	print()
	print('Add order')

	title = 'Agregar Pedido'

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewOrderForm(request.POST)

		if form.is_valid():

			form_instance = NewOrderForm(request.POST)

			form_instance.cook_id = 1


			new_order = form_instance.save()

			return HttpResponseRedirect('/orders/thanks/')


	# Create a blank form
	else:

		order = Order()

		form = NewOrderForm(instance=order)

		ctx = {
				'title': title,
				'form': form,
			}

		output = render(request, 'orders/add.html', ctx)

		return HttpResponse(output)




# Delete
def delete(request, order_id):
	print()
	print('Delete Order')

	title = 'Eliminar Pedido ?'

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
				'title': title,
				'obj': obj,
				'form': form,
		}
		output = render(request, 'orders/delete.html', ctx)
		return HttpResponse(output)



# Update
def update(request, order_id):
	print()
	print('update Order')

	title = 'Modificar Pedido'

	obj = get_object_or_404(Order, pk=order_id)

	lines = OrderLine.objects.filter(order=order_id)


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
				'title': title,
				'obj': obj,
				'form': form,
				'lines':	lines,
			}

		output = render(request, 'orders/edit.html', ctx)

		return HttpResponse(output)


# Thanks
def order_thanks(request):
	print()
	print('Orders Thanks')
	ctx = {}
	output = render(request, 'orders/thanks.html', ctx)
	return HttpResponse(output)




# ------------------------------------------------ Lines ---------------------
# Index Order Lines
def order_lines(request, order_id):
	print()
	print('Order Lines')

	order = get_object_or_404(Order, pk=order_id)  		# Get Object

	title = 'Líneas Pedido - ' + order.name

	#objs = OrderLine.objects.all()
	objs = OrderLine.objects.filter(order=order_id)

	err_msg = "No existe ningún Linea todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
			'order': order,
		}

	output = render(request, 'orders/order_lines.html', ctx)

	return HttpResponse(output)



def add_line_order(request, order_id):
	print()
	print('Add line Order')

	title = 'Agregar Línea en Pedido'

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

			return HttpResponseRedirect('/orders/thanks/')


	# Create a blank form
	else:

		line = OrderLine()

		line.order = order

		form = NewOrderLineForm(instance=line)

		ctx = {
				'title': title,
				'form': form,
				'order': order,
			}

		#output = render(request, 'lines/add.html', ctx)
		output = render(request, 'orders/order_add_line.html', ctx)

		return HttpResponse(output)

