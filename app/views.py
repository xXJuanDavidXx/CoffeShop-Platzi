from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from .models import Product


# Create your views here.

class ProductFormView(generic.FormView):
    #Parametros necesarios
    template_name ="products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('lista')


    def form_valid(slef, form):
        form.save()
        return super().form_valid(form)



class ProductList(generic.ListView):
    model = Product
    template_name = 'products/list_product.html' 
    context_object_name = 'products'





