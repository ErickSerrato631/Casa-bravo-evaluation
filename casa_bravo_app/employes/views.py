from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,

)
from .models import Empleado
from .serializers import EmployeSerializer
# Create your views here.


class EmployeListView(ListAPIView):
    serializer_class = EmployeSerializer

    def get_queryset(self):
        return Empleado.objects.all()


class EmployeCreateView(CreateAPIView):

    serializer_class = EmployeSerializer


class EmployeCreateView(CreateAPIView):

    serializer_class = EmployeSerializer

class EmployeDetailView(RetrieveAPIView):

    serializer_class = EmployeSerializer
    queryset = Empleado.objects.all()

class EmployeDeleteView(DestroyAPIView):

    serializer_class = EmployeSerializer
    queryset = Empleado.objects.all()

class EmployeUpdateView(RetrieveUpdateAPIView):

    serializer_class = EmployeSerializer
    queryset = Empleado.objects.all()