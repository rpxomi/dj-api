from rest_framework import serializers
from .models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto

        # como un DTO de Spring en Java, filtra que mostrar en la respuesta
        fields = ['id', 'titulo', 'descripcion', 'precio', 'imagen_url']

