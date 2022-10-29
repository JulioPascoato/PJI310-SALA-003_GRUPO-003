from django.db import models
import uuid

# Create your models here.


class Aula(models.Model):
    nome = models.CharField(max_length=200)
    data_aula = models.DateTimeField(null=True, blank=True)
    disciplina = models.CharField(max_length=2000, null=True, blank=True)
    conteudo = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.nome
