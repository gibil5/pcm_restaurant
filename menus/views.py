#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

#from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.http import HttpResponse


from .models import Menu


# Create your views here.

def index(request):
	#return render(request, 'menus/menus.html')

	#latest_menu_list = Menu.objects.order_by('-pub_date')[:5]
	
	latest_menu_list = Menu.objects.all()
	
	print(latest_menu_list)

	ctx = {'latest_menu_list': latest_menu_list,}
	
	output = render(request, 'menus/menus.html', ctx)

	return HttpResponse(output)



#def menu(request):
#def menu(request, menu_id):
def detail(request, menu_id):
	
	#return render(request, 'menus/menu.html')


	# Get Object
	menu = get_object_or_404(Menu, pk=menu_id)  		# Shortcut !

	ctx = {'menu': menu,}

	return	render(request, 'menus/menu.html', ctx)




#def search(request):
#	return render(request, 'menus/search.html')
