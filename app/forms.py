from django import forms
from .models import Product


#En el formulario siempre vamos a llamar los campos que definimos en nuestro modelo.
class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")  # El label se muestra en el formulario HTML
    description = forms.CharField(max_length=200, label="Descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, label="Disponible", required=False)  # Corregido `required`
    photo = forms.ImageField(label="Foto", required=False)  # Cambiado a `forms.ImageField`

    # Función para guardar los datos del formulario
    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo'],
        )


    
    
