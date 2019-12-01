


# Index
def index(request):
	print()
	print('* Pages - Index')
	
	# Init
	#menus = Menu.objects.filter(active=True)
	
	#err_msg = "No existe ningún Menú todavía."

	ctx = {
			#'menus': menus,
			#'err_msg': err_msg,
		}

	output = render(request, 'pages/home.html', ctx)

	return HttpResponse(output)
