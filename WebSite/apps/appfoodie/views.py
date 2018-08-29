from django.shortcuts import render, redirect,render_to_response
from .forms import FormularioCliente,FormularioRestaurante,FormularioProducto,FormularioPedido,FormularioModificar,FormularioModificarRes,FormularioModificarPro,FormularioModificarPed,FormularioClientes,FormularioLogin

from .models import Cliente,Restaurante,Producto,Pedido,UserProfile

from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, FormView
from django.views.generic.edit import UpdateView, DeleteView
#login
from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#registro
from django.contrib.auth.models import User
#rest-frameworl
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SurveySerializerRes,SurveySerializerPro,SurveySerializePed

import json as simplejson

@api_view(['GET', 'POST'])
def survey_listRes(request):
    if request.method == 'GET':
        stock = Restaurante.objects.all()
        serializer = SurveySerializerRes(stock, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SurveySerializerRes(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def survey_listPro(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = SurveySerializerPro(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SurveySerializerPro(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def survey_listPed(request):
    if request.method == 'GET':
        pedido = Pedido.objects.all()
        serializer = SurveySerializePed(pedido, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SurveySerializePed(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def list(request):
    stock = Restaurante.objects.all()
    stock = serializers.serialize('json',stock)
    return HttpResponse(stock, 'application/json')

def inicio(request):
	f=FormularioCliente(request.POST or None)
	context={
		"f":clientes,
	}
	return render(request,"inicio.html",context)

def listar(request):
	clientes=Cliente.objects.all()
	context={
		'clientes':clientes,
	}
	return render(request,"master.html",context)

class ClienteListView(ListView):
	model = Cliente
	template_name ='listarCli.html'

class RestauranteListView(ListView):
	model = Restaurante
	template_name ='listarRes.html'

class ProductoListView(ListView):
	model = Producto
	template_name ='listarPro.html'

class PedidoListView(ListView):
	model = Pedido
	template_name ='listarPed.html'

class CrearCliente(CreateView):
    model = Cliente
    fields = ("Nombre","Apellido","Cedula","Direccion","Telefono","Correo")
    success_url = 'listar/listarCli/'

class CrearRestaurante(CreateView):
    model = Restaurante
    fields = ("Nombre","Gerente","Direccion","Telefono")
    success_url = 'listar/listarRes/'

class CrearProducto(CreateView):
    model = Producto
    fields = ("idPro","Nombre","Precio","Descripcion","Imagen")
    success_url = reverse_lazy('LProducto')

class CrearPedido(CreateView):
    model = Pedido
    fields = ("idPed","Cliente","Cantidad","PrecioTotal")
    success_url = 'listar/listarPed/'

class Modificar(UpdateView):
    model = Cliente
    fields = ('Nombre','Apellido','Cedula','Direccion', 'Telefono','Correo')
    success_url = reverse_lazy('LCliente')

class ModificarRes(UpdateView):
    model = Restaurante
    fields=("Nombre","Gerente","Direccion","Telefono")
    success_url = reverse_lazy('LRestaurante')


class ModificarPro(UpdateView):
    model = Producto
    fields = ("idPro","Nombre","Precio","Descripcion","Imagen")
    success_url = reverse_lazy('LProducto')


class ModificarPed(UpdateView):
    model = Pedido
    fields=("idPed","Cliente","Cantidad","PrecioTotal")
    success_url = reverse_lazy('LPedido')

class EliminarCliente(DeleteView):
	model = Cliente
	success_url = reverse_lazy('LCliente')
	template_name_suffix = '_delete'

class EliminarRestaurante(DeleteView):
	model = Restaurante
	success_url = reverse_lazy('LRestaurante')
	template_name_suffix = '_delete'

class EliminarProducto(DeleteView):
	model = Producto
	success_url = reverse_lazy('LProducto')
	template_name_suffix = '_delete'

class EliminarPedido(DeleteView):
	model = Pedido
	success_url = reverse_lazy('LPedido')
	template_name_suffix = '_delete'

def registrar(request):
	if request.method == 'POST':
		r = FormularioClientes(request.POST, request.FILES)
		if r.is_valid():
			datos = r.cleaned_data

			ci = datos.get('ci')
			nombres = datos.get('nombres')
			apellidos = datos.get('apellidos')
			username = datos.get('username')
			password = datos.get('password')
			direccion = datos.get('direccion')
			email = datos.get('email')
			telefono = datos.get('telefono')
			photo = datos.get('photo')
			# Instanciamos un objeto User, con el username y password
			user_model = User.objects.create_user(username=username, password=password)
			# Añadimos datos personales
			user_model.first_name = nombres
			user_model.last_name = apellidos
			user_model.email = email
			# Y guardamos el objeto, esto guardara los datos en la db.
			user_model.save()
			# Ahora, creamos un objeto UserProfile, aunque no haya incluido
			# una imagen, ya quedara la referencia creada en la db.
			user_profile = UserProfile()
			# Al campo user le asignamos el objeto user_model
			user_profile.user = user_model
			# y le asignamos la photo (el campo, permite datos null)
			user_profile.photo = photo
			user_profile.nombres = nombres
			user_profile.apellidos = apellidos
			user_profile.direccion = direccion
			user_profile.email = email
			# Por ultimo, guardamos tambien el objeto UserProfile
			user_profile.contra = password
			user_profile.save()
			# Ahora, redireccionamos a la pagina gracias.html
			# Pero lo hacemos con un redirect.
			return redirect(reverse("Gracias", kwargs={'username':username}))
	else:
		r = FormularioClientes()
	context = {
		'r': r,
	}
	return render(request, "registrar.html", context)


def gracias(request, username):
    return render(request, "gracias.html", {'username': username})

def usuario(request):
	if request.user.is_authenticated:
		return redirect(reverse("Inicio"))

	mensaje = None
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse("Inicio"))
			else:
				mensaje = "Tu usuario esta inactivo"
		#else:
		mensaje = "Nombre de Usuario y/o Contraseña incorrecto"
	return render(request, "login.html", {"mensaje":mensaje})

def salir(request):
	logout(request)
	return redirect('Login')

def logout_view(request):
    logout(request)
    messages.success(request, 'Te has desconectado con exito.')
    return redirect('Login')
