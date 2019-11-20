def add_order(request, employee_id):
	print()
	print('Add order')

	title = 'Add Order'

	cook = get_object_or_404(Employee, pk=employee_id)  		# Get Object
	print(cook)

	table = Table.objects.first()

	# Create and populate
	if request.method == 'POST':
		print('Create and populate')

		form = lib.NewOrderForm(request.POST)

		if form.is_valid():

			form_instance = lib.NewOrderForm(request.POST)

			form_instance.cook_id = 1


			new_order = form_instance.save()

			return HttpResponseRedirect('/orders/thanks/')



	# Create a blank form
	else:

		order = Order()
		#order = Order.objects.create(cook=cook)

		#order.save()


		#form = lib.NewOrderForm(instance=order)
		form = lib.NewOrderForm(
								instance=order,
								initial={
											'cook': cook,
											'table': table,
											},
								)


		#form.cook = cook

		ctx = {
				'title': title,
				'form': form,
			}

		output = render(request, 'orders/add.html', ctx)

		return HttpResponse(output)
