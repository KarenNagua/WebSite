from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    
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
    path('listar/listarCli/modificar/<int:pk>/', views.Modificar.as_view(), name="ActualizarCli"),
    path('listar/listarRes/modificarRes/<int:pk>/', views.ModificarRes.as_view(), name="ActualizarRes"),
    path('listar/listarPro/modificarPro/<int:pk>/', views.ModificarPro.as_view(), name="ActualizarPro"),
    path('listar/listarPed/modificarPed/<int:pk>/', views.ModificarPed.as_view(), name="ActualizarPed"),
    path('listar/listarCli/eliminar/<int:pk>', views.EliminarCliente.as_view(), name="EliminarCli"),
    path('listar/listarRes/eliminarRes/<int:pk>', views.EliminarRestaurante.as_view(), name="EliminarRes"),
    path('listar/listarPro/eliminarPro/<int:pk>', views.EliminarProducto.as_view(), name="EliminarPro"),
    path('listar/listarPed/eliminarPed/<int:pk>', views.EliminarPedido.as_view(), name="EliminarPed"),
    path('gracias/<int:pk>/', views.gracias, name='Gracias'),
    path('registrar/', views.registrar),
	path('logout/', views.salir, name='Logout'),

    path('ws/restaurante/', views.survey_listRes, name='WSRestaurante'),
    path('ws/producto/', views.survey_listPro, name='WSProducto'),
    path('ws/pedido/', views.survey_listPed, name='WSPedido'),

]
