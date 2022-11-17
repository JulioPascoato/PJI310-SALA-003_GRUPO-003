from django.db import models
import uuid

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    imagem_perfil = models.ImageField(
        null=True, blank=True, upload_to='alunos/', default='professores/user-default.png')

    data_nascimento = models.DateField(blank=True, null=True)
    perfil = models.TextField(blank=True, null=True)

    celular = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(max_length=200, blank=True, null=True)

    colegio = models.CharField(max_length=200, blank=True, null=True)
    serie  = models.CharField(max_length=200, blank=True, null=True)

    dados_responsavel_1  = models.TextField(blank=True, null=True)
    dados_responsavel_2  = models.TextField(blank=True, null=True)
    
    dados_nf = models.TextField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.nome)