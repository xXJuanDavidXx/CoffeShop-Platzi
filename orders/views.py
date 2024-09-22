from django.shortcuts import render
from django.views.generic import DetailView #Esta view funciona si en la url le pasamos un argumento con el que pueda buscar esa orden.
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin


#en este caso vamos a mostrar cada orden que este activa y no requiera un flag

# Create your views here.

#Vamos a organizar la vista generica para que no necesite el arhumento pasado por url
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "my_order.html"
    context_object_name = 'order' #Con este contexto vamos a poder acceder desde el template


    #Sobreescribimos el metodo get_object para que en vez de recibir un parametro de la url, filtre por la flag definida en la db
    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first() #Filtra por ordenes activas y por usuario
    
    #Defino un contexto para pasar al template el cual define la pagina actual y sirve para mostrar el boton de mi pedido en función de si se esta en ella o no.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'miorden'
        return context

