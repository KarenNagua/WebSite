from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    #url(r'^$', 'apps.foodie.views.namevista'),
    path('', views.usuario, name='Login'),
    path('listar/', views.listar, name='Inicio'),
    path('listar/listarRes/', views.RestauranteListView.as_view(), name="LRestaurante"),
    path('listar/listarPro/', views.ProductoListView.as_view(), name="LProducto"),
    path('listar/listarPed/', views.PedidoListView.as_view(), name="LPedido"),
    path('listar/listarCli/', views.ClienteListView.as_view(), name="LCliente"),
    path('listar/listarCli/crear/', views.CrearCliente.as_view(), name="CCliente"),
    path('listar/listarRes/crearRes/', views.CrearRestaurante.as_view(), name="CRestaurante"),
    path('listar/listarPro/crearPro/', views.CrearProducto.as_view(), name="CProducto"),
    path('listar/listarPed/crearPed/', views.CrearPedido.as_view(), name="CPedido"),
    path('gracias/(?P<username>[-\w]+)/', views.gracias, name='Gracias'),
    path('registrar/', views.registrar),
	path('logout/', views.salir, name='Logout'),
]
