"""
Lines - Views
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

# Create your views here.

from orders.models import *

from orders import lib


# ------------------------------------------------ OrderLineLineLines ---------------------

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










def add(request):
	print()
	print('Add line')

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = lib.NewOrderLineForm(request.POST)

		if form.is_valid():

			form_instance = lib.NewOrderLineForm(request.POST)

			new_line = form_instance.save()

			return HttpResponseRedirect('/lines/thanks/')


	# Create a blank form
	else:

		line = OrderLine()

		form = lib.NewOrderLineForm(instance=line)

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

		form = lib.DeleteForm(request.POST)

		if form.is_valid():

			obj.delete()					# Delete !!!

			return HttpResponseRedirect('/lines/thanks/')



	# Create delete form
	else:

		form = lib.DeleteForm()

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

		form = lib.NewOrderLineForm(request.POST)

		# check whether it's valid:
		if form.is_valid():
			
			form_instance = lib.NewOrderLineForm(request.POST, instance=obj)

			form_instance.save()

			return HttpResponseRedirect('/lines/thanks/')


	# Create a blank form
	else:

		# Form from a Model
		form = lib.NewOrderLineForm(instance=obj)

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


