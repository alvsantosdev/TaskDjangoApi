
from django.db import models
import uuid

class Funcionario(models.Model):
    nome = models.CharField(max_length = 30)
    cpf = models.CharField(max_length=14)
    horas_trabalhadas = models.TimeField(null= True,  blank=True)
    salario = models.IntegerField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)





class Task(models.Model):
    nome = models.CharField(max_length= 30)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='task')
    horas = models.TimeField(null= True, blank= True)
    descricao = models.CharField(max_length= 100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


