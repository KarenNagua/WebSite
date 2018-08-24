from rest_framework import serializers
from .models import Restaurante

class SurveySerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurante
		fields = ('Nombre', 'Gerente', 'Direccion', 'Telefono')
