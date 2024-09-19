from django.contrib import admin
from django.urls import path
from .views import ProductFormView, ProductList

urlpatterns = [
        path("add_product/", ProductFormView.as_view(), name="ola"),
        path("", ProductList.as_view(), name ="lista"),
        ]
