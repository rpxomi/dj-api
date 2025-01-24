from rest_framework.viewsets import ModelViewSet
from .models import Producto
from .serializers import ProductoSerializer


# una vista, es una función que recibe una petición HTTP y devuelve una respuesta HTTP
# ¿una vista devuelve una respuesta en formato JSON? sí, en Django Rest Framework!
# cuando una vista tiene una clase definida, se le llama viewset
# un viewset, es un conjunto de vistas que se encargan de realizar operaciones CRUD (Create, Read, Update, Delete)
# y devuelve como respuesta, los datos que se han encontrados en ese consulta pero convertidos a JSON
class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all() # hace la consulta a la base de datos
    serializer_class = ProductoSerializer # convierte la respuesta a JSON

