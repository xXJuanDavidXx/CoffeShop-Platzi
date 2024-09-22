from django.urls import path   
from . import views            

urlpatterns = [
        path("mi-orden/", views.MyOrderView.as_view(), name="my_order")

        ]


