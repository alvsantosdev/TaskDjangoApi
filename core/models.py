from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.conf import settings

class User(AbstractUser):
    pass

class Funcionario(models.Model):
    cpf = models.CharField(max_length=14)
    horas_trabalhadas = models.TimeField(null= True,  blank=True)
    salario = models.IntegerField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    cargo = models.TextField(null=False, blank= False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='funcionarios')



class Task(models.Model):
    nome = models.CharField(max_length= 30)
    funcionario = models.ForeignKey("Funcionario", on_delete=models.CASCADE, related_name='tasks')
    horas = models.TimeField(null= True, blank= True)
    descricao = models.CharField(max_length= 100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


