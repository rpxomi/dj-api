from django.db import models


# un modelo, es una clase que representa una tabla que va a estar en una base de datos
class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=600)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    imagen_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo
    
