"""
Tests - Views
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django import forms

from orders.models import *
from tables.models import *
from employees.models import *
from items.models import *

import datetime
import random


# Create your views here.


# ------------------------------------------------ Forms ---------------------

class DeleteForm(forms.Form):
	pass


# ------------------------------------------------ Tests ---------------------

# Tests
def tests(request):
	print()
	print('Tests')

	title = 'Tests'

	#objs = Order.objects.exclude(state='Pagado')

	#err_msg = "No existe ningún Pedido todavía."

	ctx = {
			'title': title,
			#'objs': objs,
			#'err_msg': err_msg,
		}

	output = render(request, 'tests/tests.html', ctx)

	return HttpResponse(output)




# create orders
def create_orders(request):
	"""
	Create Random Order 
	Using:
		qty = random.randint(1, 5)
		MyModel.objects.order_by('?').first()
	"""

	print()
	print('Create Orders')
	#print('Crear Pedidos')

	objs = []

	#title = 'Create Orders'
	title = 'Crear Pedidos'


	#objs = Order.objects.exclude(state='Pagado')

	#table = get_object_or_404(Table, name='1')  		
	table = Table.objects.order_by('?').first()  	# Get a random object

	#waiter = get_object_or_404(Employee, name='Jaime')  		
	waiter = Employee.objects.filter(is_waiter=True).order_by('?').first()

	#cook = get_object_or_404(Employee, name='Gastón')  		
	cook = Employee.objects.filter(is_cook=True).order_by('?').first()



	# Create Order
	obj = Order.objects.create(
			table_id=table.id,
			waiter_id=waiter.id,
			cook_id=cook.id,
		)

	objs.append(obj)



	# Create Lines
	names = ['drinks', 'entries', 'main_courses', 'desserts', 'hot_drinks',]

	for name in names:

		family = get_object_or_404(Family, short_name=name)  		# Get Object


		count = Item.objects.filter(family_id=family.id).count()
		print(count)


		if count > 0:
			#item = get_object_or_404(Item, name=name)  		# Get Object
			#item = Item.objects.order_by('?').first()
			item = Item.objects.filter(family_id=family.id).order_by('?').first()

			qty = random.randint(1, 5)

			line = OrderLine.objects.create(
					order_id=obj.id,
					qty=qty,
					item_id=item.id,
				)


	#err_msg = "No existe ningún Pedido todavía."

	ctx = {
			'title': title,
			'objs': objs,
			#'err_msg': err_msg,
		}

	output = render(request, 'tests/create_orders.html', ctx)

	return HttpResponse(output)








# clean orders
def clean_orders(request):
	print()
	print('Clean Orders')

	today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
	objs = Order.objects.filter(date__range=(today_min, today_max))
	#print(objs)

	objs.delete()
	#print(objs)

	ctx = {}

	output = render(request, 'tests/clean_orders.html', ctx)

	return HttpResponse(output)



def clean_orders_for_today():
	print()
	print('Clean Orders')

	today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

	objs = Order.objects.filter(date__range=(today_min, today_max))
	#print(objs)

	objs.delete()
	#print(objs)




def delete_orders(request):
	print()
	print('Delete Orders')


	#item = get_object_or_404(Item, pk=item_id)


	# Create and populate
	if request.method == 'POST':
		print('mark')

		#form = DeleteItemForm(request.POST)
		form = DeleteForm(request.POST)

		if form.is_valid():

		#	item.delete()					# Delete !!!
			clean_orders_for_today()

		#	return HttpResponseRedirect('/thanks/')
			return HttpResponseRedirect('/tests/')



	# Create delete form
	else:

		#form = DeleteItemForm()
		form = DeleteForm()

		ctx = {
				#'item': item,
				'form': form,
		}
		#output = render(request, 'items/delete.html', ctx)
		output = render(request, 'tests/delete_orders.html', ctx)
		return HttpResponse(output)


