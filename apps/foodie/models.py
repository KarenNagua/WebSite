#encoding: utf-8
from django.db import models
from django.conf import settings

class Cliente(models.Model):
	Nombre = models.CharField(max_length=30,blank=True)
	Apellido = models.CharField(max_length=30,blank=True)
	Cedula = models.CharField(max_length=10)
	Direccion = models.CharField(max_length=30,blank=True)
	Telefono = models.CharField(max_length=10,blank=True)
	Correo = models.EmailField()
	def __str__(self):
		return self.Cedula


class Restaurante(models.Model):
	Nombre = models.CharField(max_length=30,blank=True)
	Gerente = models.CharField(max_length=30,blank=True)
	Direccion = models.CharField(max_length=30,blank=True)
	Telefono = models.CharField(max_length=10)

	def __str__(self):
		return self.Nombre

class Producto(models.Model):
	idPro = models.ForeignKey(Restaurante,on_delete=models.CASCADE,default="")
	Nombre = models.CharField(max_length=30,blank=True)
	Precio = models.DecimalField(max_digits=5, decimal_places=2)
	Descripcion = models.CharField(max_length=150,blank=True)
	Imagen=models.ImageField(upload_to='static',blank=True)
	def __str__(self):
		return self.Nombre

class Pedido(models.Model):
	idPed = models.ForeignKey(Producto,on_delete=models.CASCADE, default="")
	Cliente = models.CharField(max_length=30,blank=True)
	Cantidad = models.IntegerField()
	PrecioTotal = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.Cliente

class UserProfile(models.Model):
	CI= models.CharField(max_length=10)
	Nombres = models.CharField(max_length=30,blank=True)
	Apellidos = models.CharField(max_length=30,blank=True)
	Direccion = models.CharField(max_length=30,blank=True)
	Telefono = models.CharField(max_length=10,blank=True)
	Email = models.EmailField()
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='profiles', blank=True, null=True)
	contra= models.CharField(max_length=30,blank=True,default="")

	def __str__(self):
		return self.user.username
