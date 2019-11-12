from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import forms


from .models import *

# Create your views here.


# New Form
class NewEmployeeForm(forms.ModelForm):

	class Meta:

		model = Employee

		fields = [
					'name',
					'active',

					'category',
					'image',
					'description',
				]

		widgets = {          
			'image': forms.Textarea(attrs={'rows':1, 'cols':100}),  
			'description': forms.Textarea(attrs={'rows':1, 'cols':100}),  
		}


# ------------------------------------------------ Employees ---------------------

# Index
def index(request):
	print()
	print('Employees')

	
	# Employees
	objs = Employee.objects.all()
	print(objs)

	err_msg = "No existe ningún Empleado todavía."

	ctx = {
			'objs': objs,
			'err_msg': err_msg,
		}


	output = render(request, 'employees/index.html', ctx)

	return HttpResponse(output)



# Employee
def employee(request, employee_id):
	print()
	print('Employee')

	obj = get_object_or_404(Employee, pk=employee_id)  	# Get Object

	ctx = {
			#'employee': employee,
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


