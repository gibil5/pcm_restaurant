#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from employees.models import *
from orders.models import *

# Create your views here.





# ------------------------------------------------ Waiters ---------------------

# Waiters
def waiters(request):
	print()
	print('Waiters')

	title = 'Mozos'

	objs = Employee.objects.filter(is_waiter=True, active=True)

	err_msg = "No existe ningún Mozo todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'stories/waiters.html', ctx)

	return HttpResponse(output)




# Waiter
def waiter(request, waiter_id):
	print()
	print('Waiter')

	title = 'Día del Mesero'


	obj = get_object_or_404(Employee, pk=waiter_id)  		# Shortcut !


	today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
	orders = Order.objects.filter(waiter=waiter_id, date__range=(today_min, today_max))

	err_msg = "Mozo no existe."
	
	err_msg_orders = "No existe ningún Pedido Abierto."

	
	ctx = {
			'title': title,
			'obj': obj,
			'orders': orders,
			'err_msg': err_msg,
			'err_msg_orders': err_msg_orders,
		}

	output = render(request, 'stories/waiter.html', ctx)

	return HttpResponse(output)




# ------------------------------------------------ Cooks ---------------------

# Cooks
def cooks(request):
	print()
	print('Cooks')

	title = 'Cocineros'

	objs = Employee.objects.filter(is_cook=True, active=True)

	err_msg = "No existe ningún Cocinero todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'stories/cooks.html', ctx)

	return HttpResponse(output)



# Cook
def cook(request, cook_id):
	print()
	print('Cook')

	title = 'Día del Cocinero'


	obj = get_object_or_404(Employee, pk=cook_id)  		# Shortcut !


	today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
	today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

	orders = Order.objects.filter(cook=cook_id, date__range=(today_min, today_max))


	err_msg = "Cocinero no existe."

	ctx = {
			'title': title,
			'obj': obj,
			'orders': orders,
			'err_msg': err_msg,
		}



	#output = render(request, 'stories/waiter.html', ctx)
	output = render(request, 'stories/cook.html', ctx)

	return HttpResponse(output)




# ------------------------------------------------ Stories ---------------------

# Index
def index(request):
	print()
	print('Index')

	title = 'Hello Stories !'

	#objs = Order.objects.exclude(state='Pagado')

	#err_msg = "No existe ningún Pedido todavía."

	ctx = {
			'title': title,
			#'objs': objs,
			#'err_msg': err_msg,
		}

	output = render(request, 'stories/index.html', ctx)

	return HttpResponse(output)
