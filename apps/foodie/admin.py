from django.contrib import admin
from .models import Cliente
from .models import Pedido
from .models import Restaurante
from .models import Producto
from .models import UserProfile

#class AdminUserProfile(admin.ModelAdmin):
	#list_display=["__str__","Nombre","user"]
	#model=UserProfile

admin.site.register(UserProfile)

class AdminCliente(admin.ModelAdmin):
	list_display=["__str__","Nombre","Apellido","Cedula","Direccion","Telefono","Correo"]
	list_filter=["Nombre"]
	search_fields=["Nombre"]
	class Meta:
		model=Cliente

admin.site.register(Cliente,AdminCliente)

class AdminPedido(admin.ModelAdmin):
	list_display=["__str__","Cliente","Cantidad","PrecioTotal"]
	class Meta:
		model=Pedido

admin.site.register(Pedido,AdminPedido)

class AdminRestaurante(admin.ModelAdmin):
	list_display=["__str__","Nombre","Gerente","Direccion","Telefono"]
	class Meta:
		model=Restaurante

admin.site.register(Restaurante,AdminRestaurante)


class AdminProducto(admin.ModelAdmin):
	list_display=["__str__","Nombre","Precio","Descripcion","Imagen"]
	class Meta:
		model=Producto

admin.site.register(Producto,AdminProducto)
