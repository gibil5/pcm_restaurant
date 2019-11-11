from .models import *

def get_items_dic():

	#families = Family.objects.all()
	families = Family.objects.filter(active=True)

	items_dic = {}
	for fam in families:
	
		#items = Item.objects.filter(family=fam.id)
		items = Item.objects.filter(family=fam.id, active=True)
	
		items_dic[fam.name] = items
	return items_dic
