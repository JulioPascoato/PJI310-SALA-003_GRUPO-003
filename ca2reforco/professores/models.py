from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.


class Professor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    localizacao = models.CharField(max_length=200, blank=True, null=True)
    introducao = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    imagem_perfil = models.ImageField(
        null=True, blank=True, upload_to='professores/', default='professores/user-default.png')
    endereco = models.TextField(blank=True, null=True)
    telefone = models.CharField(max_length=200, blank=True, null=True)
    celular = models.CharField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=200, blank=True, null=True)
    rg = models.CharField(max_length=200, blank=True, null=True)
    pis = models.CharField(max_length=200, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    dados_bancarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class Habilidade(models.Model):
    owner = models.ForeignKey(
        Professor, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    descricao = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.nome)
