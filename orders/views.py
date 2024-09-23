from django.shortcuts import render
from django.views.generic import DetailView, CreateView  #DetailView funciona si en la url le pasamos un argumento con el que pueda buscar esa orden.
from .models import Order, OrderProduct
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateOrderForm
from django.urls import reverse_lazy


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



#Creamos la vista para agregar poroductos a la orden o crar la orden, esta hereda de LoginRequeridMixin y CratedView
class CreateOrderProduct(LoginRequiredMixin, CreateView):
    #recivimos los parametros necesarios que requiere la vista.
    form_class = CreateOrderForm #Formulario
    template_name = 'create_order.html' # Template
    success_url = reverse_lazy('my_order') #Donde vamos a rediriir al user

    def form_valid(self, form): #Sobre escribimos el metodo form_valid
        order, _ = Order.objects.get_or_create( #Django nos permite obtener o crear esto es para que en caso de que la orden no este creada, se cree.(Camibia created por _ porque en este caso no se usa)
                is_active = True,
                user = self.request.user,
                ) #Los parametros que nesecitamos poner en la orden, activa y el usuario que la pide.
        
        form.instance.order = order #Asocia el producto que se está creando (representado por form.instance) con la orden obtenida o creada anteriormente.
        form.instance.quantity = 1 #Establece la cantidad del producto a 1. Esto podría ser configurable en el formulario, pero aquí se establece un valor por defecto.
        form.save() # Guarda los datos del formulario en la base de datos, creando un nuevo registro de producto asociado a la orden.
        return super().form_valid(form) #Llama al método form_valid de la clase base CreateView, que se encarga de la redirección a la URL de éxito definida anteriormente.
        #No se debe olvidar el return, si no la función no va a devolver nada.


