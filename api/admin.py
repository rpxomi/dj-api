from django.contrib import admin
from .models import Producto

# para tener acceso a los productos, en el admin de django
admin.site.register(Producto)

