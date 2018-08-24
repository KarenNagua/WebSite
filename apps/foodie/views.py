from django.shortcuts import render, redirect,render_to_response
from .forms import FormularioCliente,FormularioRestaurante,FormularioProducto,FormularioPedido,FormularioModificar,FormularioModificarRes,FormularioModificarPro,FormularioModificarPed,FormularioClientes,FormularioLogin

from .models import Cliente,Restaurante,Producto,Pedido,UserProfile

from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
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
from .serializers import SurveySerializer

import json as simplejson

@api_view(['GET', 'POST'])
def survey_list(request):
    if request.method == 'GET':
        stock = Restaurante.objects.all()
        serializer = SurveySerializer(stock, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SurveySerializer(data=request.DATA)
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
	form_class = FormularioCliente
	#fields = ['Nombre','Apellido','Cedula','Direccion', 'Telefono','Correo']
	template_name = 'crear.html'
    #success_url = 'listarCli'

class CrearRestaurante(CreateView):
    model = Restaurante
    template_name = 'crearRes.html'
    success_url = '/foodie/listar/listarRes/'
    fields = ("Nombre","Gerente","Direccion","Telefono")

class CrearProducto(CreateView):
	form_class = FormularioProducto
	template_name = 'crearPro.html'
    #success_url = 'listarPro'

class CrearPedido(CreateView):
    form_class = FormularioPedido
    template_name = 'crearPed.html'
    #success_url = 'listarPed'

class Modificar(UpdateView):
    model = Cliente
    #fields = ['Nombre','Apellido','Cedula','Direccion', 'Telefono','Correo']
    template_name = 'modificar.html'
    #success_url = ''

    def get_success_url(self):
        return self.request.path

class ModificarRes(UpdateView):
    model = Restaurante
    template_name = 'modificarRes.html'
    #success_url = ''

    def get_success_url(self):
        return self.request.path

class ModificarPro(UpdateView):
    model = Producto
    template_name = 'modificarPro.html'
    #success_url = ''

    def get_success_url(self):
        return self.request.path

class ModificarPed(UpdateView):
    model = Pedido
    template_name = 'modificarPed.html'
    #success_url = ''

    def get_success_url(self):
        return self.request.path

class EliminarCliente(DeleteView):
	model = Cliente
	success_url = "listarCli"
	template_name = 'deleteCli'

class EliminarRestaurante(DeleteView):
	model = Restaurante
	success_url = "listarRes"
	template_name = 'deleteRes.html'

class EliminarProducto(DeleteView):
	model = Producto
	success_url = "listarPro"
	template_name = 'deleteProd.html'

class EliminarPedido(DeleteView):
	model = Pedido
	success_url = "listarPed"
	template_name = 'deletePed.html'

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

def list(request):
    clientes = Cliente.objects.all() #Modelo del que van a sacar el json
    mresult = []
    mreturn = {}
    for m in clientes:
         mresult.append({"Nombre": m.Nombre,
         "Apellido": m.Apellido,
         "Cedula": m.Cedula,
         "Direccion": m.Direccion,
         "Telefono": m.Telefono,
         "Correo": m.Correo})
    mreturn['Cliente'] = mresult
    return HttpResponse(simplejson.dumps(mreturn),'application/json')

def listRes(request):
    restaurantes = Restaurante.objects.all()
    mresult = []
    mreturn = {}
    for m in restaurantes:
        mresult.append({"Nombre": m.Nombre,
        "Gerente": m.Gerente,
        "Direccion": m.Direccion,
        "Telefono": m.Telefono})
        mreturn['Restaurante'] = mresult
    return HttpResponse(simplejson.dumps(mreturn),'application/json')

def listPro(request):
	productos= Producto.objects.all()
	mresult = []
	mreturn = {}
	for m in productos:
	    mresult.append({"Nombre": m.Nombre,
	    "Precio": str(m.Precio),
	    "Descripcion": m.Descripcion,
	    "Imagen":str(m.Imagen)})
	    mreturn['Producto'] = mresult
	return HttpResponse(simplejson.dumps(mreturn),'application/json')


def listPed(request):
	pedidos= Pedido.objects.all()
	mresult = []
	mreturn = {}
	for m in pedidos:
	    mresult.append({"Cliente": m.Cliente,
	    "Cantidad": m.Cantidad,
	    "Precio Total": str(m.PrecioTotal)})
	    mreturn['Producto'] = mresult
	return HttpResponse(simplejson.dumps(mreturn),'application/json')

def listUser(request):
	users= UserProfile.objects.all()
	mresult = []
	mreturn = {}
	for m in users:
	    mresult.append({"Usuario": str(m.user),
	    "Contra": m.contra})
	    mreturn['Usuarios'] = mresult
	return HttpResponse(simplejson.dumps(mreturn),'application/json')

@api_view(['GET', 'POST'])
def survey_list(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = SurveySerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SurveySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def logout_view(request):
    logout(request)
    messages.success(request, 'Te has desconectado con exito.')
    return redirect('Login')
