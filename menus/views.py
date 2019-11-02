#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

#from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.http import HttpResponse


from .models import Menu

from items import lib

# Create your views here.


def add(request):

	menu = Menu.objects.create()

	ctx = {
			'menu': menu,
			}

	output = render(request, 'menus/add.html', ctx)

	return HttpResponse(output)



def index(request):
	
	latest_menu_list = Menu.objects.all()
	print(latest_menu_list)

	ctx = {
			'latest_menu_list': latest_menu_list,
			}

	output = render(request, 'menus/menus.html', ctx)

	return HttpResponse(output)



def detail(request, menu_id):
	print()
	print('Menu - Detail')
	print()

	menu = get_object_or_404(Menu, pk=menu_id)  		# Shortcut !
	print(menu)

	print(menu.entries.all())
	print(menu.main_courses.all())
	print(menu.desserts.all())
	print()

	ctx = {'menu': menu,}

	return	render(request, 'menus/menu.html', ctx)




