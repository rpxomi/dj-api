from django.urls import path
from .views import ProductoViewSet


# al ingresar a la ruta api/productos/, se va a ejecutar la vista: ProductoViewSet
# la vista, es el tipo de respuesta que se va a dar (obtiene todos los productos y los convierte a JSON)
# name, es el nombre que se le da a la vista, para poder referenciarla dentro de la aplicación
urlpatterns = [
    # list, es para obtener todos los productos
    path('productos/', ProductoViewSet.as_view({'get': 'list'}), name='productos'),

    # retrieve, es para obtener un solo producto por su id
    path('producto/<int:pk>/', ProductoViewSet.as_view({'get': 'retrieve'}), name='producto'),
]

