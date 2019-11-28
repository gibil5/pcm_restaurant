from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


from orders.models import *

from tables.models import *

from employees.models import *

from items.models import *



import datetime


# Create your views here.


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




# clean orders
def clean_orders(request):
	print()
	print('Clean Orders')

	today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

	objs = Order.objects.filter(date__range=(today_min, today_max))
	print(objs)

	objs.delete()
	print(objs)


	ctx = {
		}

	output = render(request, 'tests/clean_orders.html', ctx)

	return HttpResponse(output)




# create_orders
def create_orders(request):
	print()
	print('jx - Create Orders')

	objs = []


	title = 'Create Orders'

	#objs = Order.objects.exclude(state='Pagado')


	table = get_object_or_404(Table, name='1')  		# Get Object

	waiter = get_object_or_404(Employee, name='Jaime')  		# Get Object

	cook = get_object_or_404(Employee, name='Gastón')  		# Get Object




	#obj = Order()
	obj = Order.objects.create(
			table_id=table.id,
			waiter_id=waiter.id,
			cook_id=cook.id,
		)
	objs.append(obj)



	# Lines
	#names = ['Causa', 'Sancochado', 'Helado', "Café", ]
	#names = ['Causa', 'Sancochado', 'Helado',]
	#names = ['Entradas', 'Platos de Fondo', 'Postres',]
	#names = ['Entradas',]

	#names = ['Entradas', 'Postres', 'Platos de Fondo', 'Bebidas Calientes' ]
	names = ['entries', 'main_courses', 'desserts', 'hot_drinks', ]


	for name in names:

		#item = get_object_or_404(Item, name=name)  		# Get Object


		family = get_object_or_404(Family, short_name=name)  		# Get Object


		#MyModel.objects.order_by('?').first()
		#item = Item.objects.order_by('?').first()
		item = Item.objects.filter(family_id=family.id).order_by('?').first()



		line = OrderLine.objects.create(
				order_id=obj.id,
				qty=3,
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




