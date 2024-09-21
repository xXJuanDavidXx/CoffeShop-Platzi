from django.contrib import admin
from .models import Order, OrderProduct

# Register your models here.

#Aqui van los detalles de la orden y es un inline que se va a agregar a la clase padre para poder visualizar en detalle
class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


#Esta es la tabla padre donde esta la orden
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines= [
        OrderProductInlineAdmin #Agrega la tabla OrderProduct a la tabla Order. 
            ]

admin.site.register(Order,OrderAdmin) 



