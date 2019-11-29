from django import forms
from django.forms import modelform_factory, modelformset_factory

from .models import *

# ------------------------------------------------ Classes ---------------------
class DeleteMenuForm(forms.Form):
	pass
	#your_name = forms.CharField(label='Your name', max_length=100)


class MenuForm(forms.ModelForm):
	#print()
	#print('MenuForm')

	#def __init__(self, *args, **kwargs):
	#	print('MF - Init')		
	#	super().__init__(*args, **kwargs)

	class Meta:

		model = Menu

		fields = [
					'name',
					'date',
					'family',
					#'family_id', # Dep
					'items',
				]
	
	name = forms.CharField(max_length=100, label='Nombre')
	
	date = forms.DateField(required=False, label='Fecha')
	
	#family = forms.CharField(max_length=100, label='Familia')

	#family_id = forms.IntegerField()

	#items = forms.ModelMultipleChoiceField(queryset=Item.objects.filter(family=1), widget=forms.widgets.CheckboxSelectMultiple)
	#items = forms.ModelMultipleChoiceField(queryset=Item.objects.filter(family=family_id), widget=forms.widgets.CheckboxSelectMultiple)
	items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple, label='Platos')



# New Form
class NewMenuForm(forms.ModelForm):
	#print()
	#print('NewMenuForm')

	class Meta:

		model = Menu

		fields = [
					'name',
					'date',
				]
