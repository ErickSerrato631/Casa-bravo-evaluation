from rest_framework import serializers
from .models import Empleado
from datetime import date
from dateutil.relativedelta import relativedelta

class EmployeSerializer(serializers.ModelSerializer):

    edad = serializers.SerializerMethodField()
    tiempo_laboral = serializers.SerializerMethodField()
    fecha_retiro = serializers.SerializerMethodField()

    class Meta:
        model = Empleado
        #fields = (
        #    'id',
        #    'nombre',
        #    'apellido_paterno',
        #    'apellido_materno',
        #    'fecha_nacimiento',
        #    'fecha_ingreso_laboral'
        #)
        fields= ('__all__')

    def get_edad(self, object):
        hoy =  date.today()
        nacimiento = object.fecha_nacimiento

        años= ((hoy-nacimiento).total_seconds()/ (365.242*24*3600))
        añosInt=int(años)

        meses=(años-añosInt)*12
        mesesInt=int(meses)

        dias=(meses-mesesInt)*(365.242/12)
        diasInt=int(dias)

        edad = str(añosInt) + " años, " + str(mesesInt) + " meses y " + str(diasInt)+ " días" 

        return edad

    def get_tiempo_laboral(self, object):
        hoy =  date.today()

        ingreso = object.fecha_ingreso_laboral

        años= ((hoy-ingreso).total_seconds()/ (365.242*24*3600))
        añosInt=int(años)

        meses=(años-añosInt)*12
        mesesInt=int(meses)

        dias=(meses-mesesInt)*(365.242/12)
        diasInt=int(dias)

        tiempo_laboral = str(añosInt) + " años, " + str(mesesInt) + " meses y " + str(diasInt)+ " días" 
        return tiempo_laboral

    def get_fecha_retiro(self, object):

        #Calculamos en que año el empleado tiene 65 años y 66 años con 5 meses 
        nacimiento = object.fecha_nacimiento
        fecha_edad_65 = nacimiento.replace(year=nacimiento.year+65)
        fecha_edad_66 = nacimiento.replace(year=nacimiento.year+66)
        fecha_edad_66=  fecha_edad_66 + relativedelta(months=5)

        #Calculamos en que año el empleado cumple 37 años laborando
        ingreso= object.fecha_ingreso_laboral
        laborando_37_años =  ingreso.replace(year=ingreso.year+37)


        #Obtenemos la diferencia de fechas del tiempo laborado contra la edad para jubilarse comparamos

        años= ((fecha_edad_65-laborando_37_años).total_seconds()/ (365.242*24*3600))
        añosInt=int(años)

        meses=(años-añosInt)*12
        mesesInt=int(meses)

        dias=(meses-mesesInt)*(365.242/12)
        diasInt=int(dias)


        if añosInt >= 0 and  mesesInt>=0 and diasInt>=0:
            print(fecha_edad_65)
            return fecha_edad_65

        else:

            print(fecha_edad_66)
            return fecha_edad_66

        