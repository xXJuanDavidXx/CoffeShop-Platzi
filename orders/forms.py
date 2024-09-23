from django import forms
from .models import OrderProduct

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['product'] 
       

