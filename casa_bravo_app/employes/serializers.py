from rest_framework import serializers
from .models import Empleado

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = (
            'id',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_nacimiento',
            'fecha_ingreso_laboral',
        )
#      fields= ('__all__')