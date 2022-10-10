from django.urls import path
from .views import vehiculoView

urlpatterns= [
    path('vehiculos/', vehiculoView.as_view(), name='vehiculos_list'),
    path('vehiculos/<int:id>', vehiculoView.as_view(), name='vehiculos_process'),
]