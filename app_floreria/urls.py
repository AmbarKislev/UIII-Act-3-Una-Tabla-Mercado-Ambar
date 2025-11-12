from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pedido/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedido/ver/', views.ver_pedido, name='ver_pedido'),
    path('pedido/actualizar/<int:id_pedido>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedido/borrar/<int:id_pedido>/', views.borrar_pedido, name='borrar_pedido'),
]
