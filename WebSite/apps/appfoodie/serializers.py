from rest_framework import serializers
from .models import Restaurante,Producto,Pedido

class SurveySerializerRes(serializers.ModelSerializer):
	class Meta:
		model = Restaurante
		fields = ('Nombre', 'Gerente', 'Direccion', 'Telefono')

class SurveySerializerPro(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields=("idPro","Nombre","Precio","Descripcion","Imagen")

class SurveySerializePed(serializers.ModelSerializer):
	class Meta:
		model = Pedido
		fields=("idPed","Cliente","Cantidad","PrecioTotal")
