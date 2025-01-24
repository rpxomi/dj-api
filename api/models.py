from django.db import models


# un modelo, es una clase que representa una tabla que va a estar en una base de datos
class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    # representa un número con decimales, ejemplo: 10.5
    precio = models.FloatField()

    def __str__(self):
        return self.nombre
    
