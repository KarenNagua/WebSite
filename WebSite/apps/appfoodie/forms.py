#encoding: utf-8
from django import forms
from .models import Cliente,Restaurante,Pedido,Producto,UserProfile
from django.contrib.auth.models import User

class FormularioCliente(forms.ModelForm):
	class Meta:
		model=Cliente
		fields=["Nombre","Apellido","Cedula","Direccion","Telefono","Correo"]

class FormularioRestaurante(forms.ModelForm):
	class Meta:
		model=Restaurante
		fields=["Nombre","Gerente","Direccion","Telefono"]

class FormularioProducto(forms.ModelForm):
	class Meta:
		model=Producto
		fields=["idPro","Nombre","Precio","Descripcion","Imagen"]


class FormularioPedido(forms.ModelForm):
	class Meta:
		model=Pedido
		fields=["idPed","Cliente","Cantidad","PrecioTotal"]

class FormularioModificar(forms.ModelForm):
	class Meta:
		model=Cliente
		fields=["Nombre","Apellido","Cedula","Direccion","Telefono","Correo"]

class FormularioModificarRes(forms.ModelForm):
	class Meta:
		model=Restaurante
		fields=["Nombre","Gerente","Direccion","Telefono"]
class FormularioModificarPro(forms.ModelForm):
	class Meta:
		model=Producto
		fields=["Nombre","Precio","Descripcion","Imagen"]

class FormularioModificarPed(forms.ModelForm):
	class Meta:
		model=Pedido
		fields=["Cliente","Cantidad","PrecioTotal"]


class FormularioClientes(forms.Form):
	ci = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	nombres = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	apellidos = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
	username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	direccion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	telefono = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	photo = forms.ImageField(required=False)

	def clean_username(self):
		username = self.cleaned_data['username']
		if  User.objects.filter(username=username):
			raise forms.ValidationError("Nombre de usuario ya registrado.")
		return username

	def clean_email(self):
		#Comprueba que no exista un email igual
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			raise forms.ValidationError("Ya existe un email igual.")
		return email

	def clean_password2(self):
		password = self.cleaned_data['password']
		password2 = self.cleaned_data['password2']
		if password != password2:
			raise forms.ValidationError("La contraseña no coincide.")
		return password2

class FormularioLogin(forms.Form):
	username = forms.CharField(max_length=30,
widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(max_length=32,
widget=forms.PasswordInput(attrs={'class': 'form-control'}))
