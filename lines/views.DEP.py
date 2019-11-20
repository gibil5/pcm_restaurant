# Update Served
def update_served(request, line_id):
	print()
	print('update Line Served')

	obj = get_object_or_404(OrderLine, pk=line_id)

	obj.state = 'served'
	obj.save()

	return HttpResponseRedirect('/lines/thanks/')


# Update Ready
def update_ready(request, line_id):
	print()
	print('update Line Ready')

	obj = get_object_or_404(OrderLine, pk=line_id)

	obj.state = 'ready'
	obj.save()

	return HttpResponseRedirect('/lines/thanks/')



# Update Preparation
def update_preparation(request, line_id):
	print()
	print('update Line Preparation')

	obj = get_object_or_404(OrderLine, pk=line_id)

	obj.state = 'preparation'
	obj.save()

	return HttpResponseRedirect('/lines/thanks/')
