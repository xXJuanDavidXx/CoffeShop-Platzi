from django.db import models
from app.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order_date = models.DateTimeField(auto_now_add=True)

    #Le estamos agregando un formato a la forma en la que se va 
    def __str__(self):
        return f"order {self.id} by {self.user}"




class OrderProduct(models.Model):
    orden = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()


    def __str__(self) -> str:
        return f"{self.orden} - {self.product}"



