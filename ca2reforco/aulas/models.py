from django.db import models
import uuid
from professores.models import Professor
from alunos.models import Aluno

# Create your models here.


class Aula(models.Model):
    professor = models.ForeignKey(
        Professor, null=True, blank=True, on_delete=models.RESTRICT)
    aluno = models.ForeignKey(
        Aluno, null=True, blank=True, on_delete=models.RESTRICT)
    nome = models.CharField(max_length=200)
    data_aula = models.DateTimeField(null=True, blank=True)
    disciplina = models.CharField(max_length=2000, null=True, blank=True)
    conteudo = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    pacote = models.ForeignKey(
        'Pacote', on_delete=models.PROTECT, blank=True, null=True)
    sala = models.ForeignKey(
        'Sala', on_delete=models.PROTECT, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.nome


class Pacote(models.Model):
    tipo = models.CharField(max_length=200)
    quantidade_aulas = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.tipo


class Sala(models.Model):
    nome = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.nome
