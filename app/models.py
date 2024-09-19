from django.db import models

class Product(models.Model):  # Hereda de models.Model
    name = models.CharField(max_length=200, verbose_name="nombre") 
    description = models.TextField(verbose_name="descripción")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="precio")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    photo = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="foto")

    def __str__(self):
        return self.name

