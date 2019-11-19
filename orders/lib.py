from django import forms
from .models import *




# ------------------------------------------------ Forms ---------------------

# Order
class NewOrderForm(forms.ModelForm):

	class Meta:

		model = Order

		fields = [
					'date',
					'state',

					'active',
					'table',
					'waiter',
					'cook',
				]

	#items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple, label='Platos')


#class DeleteForm(forms.Form):
#	pass


# Order Line
class NewOrderLineForm(forms.ModelForm):

	class Meta:

		model = OrderLine

		fields = [
					#'name',
					'order',
					'item',
					'qty',
				]

	#items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), widget=forms.widgets.CheckboxSelectMultiple, label='Platos')



# Delete
class DeleteForm(forms.Form):
	pass

