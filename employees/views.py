from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms


from .models import *

# Create your views here.


# ------------------------------------------------ Employees ---------------------

def employees(request):
	print()
	print('Employees')

	
	# Employees
	employees = Employee.objects.all()

	err_msg = "No existe ningún Empleado todavía."

	ctx = {
			'employees': employees,
			'err_msg': err_msg,
		}


	output = render(request, 'employees/employees.html', ctx)

	return HttpResponse(output)



def employee(request, employee_id):
	print()
	print('Employee')

	employee = get_object_or_404(Employee, pk=employee_id)  	# Get Object


	ctx = {
			'employee': employee,
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

			return HttpResponseRedirect('/thanks/')

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


	employee = get_object_or_404(Employee, pk=employee_id)


	# Create and populate
	if request.method == 'POST':
		print('mark')

		form = DeleteEmployeeForm(request.POST)

		if form.is_valid():

			employee.delete()					# Delete !!!

			return HttpResponseRedirect('/thanks/')



	# Create delete form
	else:

		form = DeleteEmployeeForm()

		ctx = {
				'employee': employee,
				'form': form,
		}
		output = render(request, 'employees/delete.html', ctx)
		return HttpResponse(output)





def update(request, employee_id):
	print()
	print('update Employee')

	employee = get_object_or_404(Employee, pk=employee_id)


	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = NewEmployeeForm(request.POST)

		# check whether it's valid:
		if form.is_valid():
			
			form_instance = NewEmployeeForm(request.POST, instance=employee)

			form_instance.save()

			#return HttpResponseRedirect('/thanks/')
			return HttpResponseRedirect('/employees/thanks/')


	# Create a blank form
	else:

		# Form from a Model
		form = NewEmployeeForm(instance=employee)

		form.fields['name'].label = "Nombre"

		# Context
		ctx = {
				'employee': employee,
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


