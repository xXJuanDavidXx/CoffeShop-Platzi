from django.contrib import admin
from .models import Product


# Register your models here.
class ProductsAdmin(admin.ModelAdmin): #Heredamos de una calse que nos permite registrar modelos en el admin
    model = Product
    list_display = ['name','price'] # esto nos permite mostar los campos que queramos en el admin de django.
    search_fields = ['name'] # Esto nos permite hacer busquedas, en este caso por nombre.

admin.site.register(Product, ProductsAdmin) #Esto es importante para registrar el modelo, y con la clase nos permite ralizar modificacipnes en el admin.






