from django import forms
from .models import *




# ------------------------------------------------ Forms ---------------------

# Order
class NewOrderForm(forms.ModelForm):

	class Meta:

		model = Order

		fields = [
					'date',
					'waiter',
					'state',
					'active',
					'table',
					'cook',
				]

	#items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple, label='Platos')




# Order Line
class NewOrderLineForm(forms.ModelForm):

	class Meta:

		model = OrderLine

		fields = [
					#'name',
					'order',
					'item',
					'qty',
					'state',
				]

	#items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple, label='Platos')



# Delete
class DeleteForm(forms.Form):
	pass


