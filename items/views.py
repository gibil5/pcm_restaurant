#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from .models import *

from . import lib

def index(request):
	print()
	print('Item - Index')

	#return render(request, 'items/items.html')
	

	# Items
	items_dic = lib.get_items_dic()
	print(items_dic)



	# Items
	item_list = Item.objects.order_by('family')
	#print(item_list)
	
	ctx = {
			#'families': families,
			#'item_list': item_list,
			'items_dic': items_dic,
			}

	output = render(request, 'items/items.html', ctx)
	#print(output)

	return HttpResponse(output)


def detail(request, item_id):
	
	# Get Object
	item = get_object_or_404(Item, pk=item_id)  		# Shortcut !

	ctx = {'item': item,}

	return	render(request, 'items/item.html', ctx)




def about(request):

	return render(request, 'items/about.html')



#def admin(request):

#	return render(request, 'items/admin.html')
