from .models import *

def get_items_dic():

	families = Family.objects.all()

	items_dic = {}
	for fam in families:
		items = Item.objects.filter(family=fam.id)
		items_dic[fam.name] = items
	return items_dic
