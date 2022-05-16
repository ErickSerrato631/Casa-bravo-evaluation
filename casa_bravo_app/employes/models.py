from django.db import models

# Create your models here.

class Empleado(models.Model):

    nombre = models.CharField(
        verbose_name= 'Nombre(s)',
        max_length= 45
        )
    apellido_paterno = models.CharField(
        verbose_name= 'Apellido paterno',
        max_length= 45,
        blank= True,
        null= True
        )
    apellido_materno = models.CharField(
        verbose_name= 'Apellido materno',
        max_length= 45,
        blank= True,
        null= True
        )

    fecha_nacimiento = models.DateField()

    fecha_ingreso_laboral = models.DateField()


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return str(self.nombre)+ "  " + str(self.apellido_paterno)+ "  " + str(self.apellido_materno)