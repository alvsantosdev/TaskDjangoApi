from .models import Funcionario, Task
from rest_framework import serializers


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class FuncionarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
