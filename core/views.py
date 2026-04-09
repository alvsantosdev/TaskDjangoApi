from django.shortcuts import render
from rest_framework import viewsets

from .models import Funcionario, Task
from.serializers import FuncionarioSerializers, TaskSerializers

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializers

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers


