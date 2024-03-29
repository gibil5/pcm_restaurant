"""
Employees - Views
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

from .models import *


# Create your views here.




# ------------------------------------------------ Forms ---------------------
# New Form
class NewEmployeeForm(forms.ModelForm):

	class Meta:

		model = Employee

		fields = [
					'name',
					'active',
					'is_waiter',
					'is_cook',
					'image',
					'description',
				]

		widgets = {          
			'image': forms.Textarea(attrs={'rows':1, 'cols':100}),  
			'description': forms.Textarea(attrs={'rows':1, 'cols':100}),  
		}


class DeleteForm(forms.Form):
	pass



# ------------------------------------------------ Employees ---------------------

# Index
def index(request):
	print()
	print('Employees')

	title = 'Empleados'


	objs = Employee.objects.all()


	err_msg = "No existe ningún Empleado todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'employees/index.html', ctx)

	return HttpResponse(output)



# Waiters
def waiters(request):
	print()
	print('Waiters')

	title = 'Mozos'

	# Categ
	#category = Category.objects.filter(name='Mozo')[0]
	#print(category)


	# Cooks
	#objs = Employee.objects.filter(category=category.id)
	objs = Employee.objects.filter(is_waiter=True)
	print(objs)

	err_msg = "No existe ningún Mozo todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'employees/index.html', ctx)

	return HttpResponse(output)



# Cooks
def cooks(request):
	print()
	print('Cooks')

	title = 'Cocineros'

	# Categ
	#category = Category.objects.filter(name='Cocinero')[0]
	#print(category)


	# Cooks
	#objs = Employee.objects.filter(category=category.id)
	objs = Employee.objects.filter(is_cook=True)
	print(objs)

	err_msg = "No existe ningún Cocinero todavía."

	ctx = {
			'title': title,
			'objs': objs,
			'err_msg': err_msg,
		}

	output = render(request, 'employees/index.html', ctx)

	return HttpResponse(output)




# Employee
def employee(request, employee_id):

	obj = get_object_or_404(Employee, pk=employee_id)  	# Get Object

	ctx = {
			'obj': obj,
			}

	return	render(request, 'employees/employee.html', ctx)





def add(request):
	print()
	print('Add employee')

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewEmployeeForm(request.POST)

		if form.is_valid():

			form_instance = NewEmployeeForm(request.POST)

			new_employee = form_instance.save()

			return HttpResponseRedirect('/employees/thanks/')

	# Create a blank form
	else:

		employee = Employee()

		form = NewEmployeeForm(instance=employee)

		ctx = {
				'form': form,
			}

		output = render(request, 'employees/add.html', ctx)

		return HttpResponse(output)








def delete(request, employee_id):
	print()
	print('Delete Employee')


	obj = get_object_or_404(Employee, pk=employee_id)


	# Create and populate
	if request.method == 'POST':
		print('mark')

		form = DeleteForm(request.POST)

		if form.is_valid():

			obj.delete()					# Delete !!!

			return HttpResponseRedirect('/employees/thanks/')



	# Create delete form
	else:

		form = DeleteForm()

		ctx = {
				'obj': obj,
				'form': form,
		}
		output = render(request, 'employees/delete.html', ctx)
		return HttpResponse(output)




# Update
def update(request, employee_id):
	print()
	print('update Employee')


	obj = get_object_or_404(Employee, pk=employee_id)


	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewEmployeeForm(request.POST)

		# check whether it's valid:
		if form.is_valid():
			
			form_instance = NewEmployeeForm(request.POST, instance=obj)

			form_instance.save()

			return HttpResponseRedirect('/employees/thanks/')


	# Create a blank form
	else:

		# Form from a Model
		form = NewEmployeeForm(instance=obj)

		# Context
		ctx = {
				'obj': obj,
				'form': form,
			}

		output = render(request, 'employees/edit.html', ctx)

		return HttpResponse(output)



def employee_thanks(request):
	print()
	print('Employees Thanks')
	ctx = {}
	output = render(request, 'employees/thanks.html', ctx)
	return HttpResponse(output)


