from django.urls import path   
from . import views            

urlpatterns = [
        path("mi-orden/", views.MyOrderView.as_view(), name="my_order"),
        path("crear_orden/", views.CreateOrderProduct.as_view(), name="crear_orden"),
        ]


