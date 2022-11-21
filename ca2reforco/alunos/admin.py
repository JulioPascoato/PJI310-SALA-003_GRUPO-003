from django.contrib import admin
from .models import Aluno

# Register your models here.


class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "celular", "data_nascimento",
                    "dados_responsavel_1", "endereco")
    list_filter = ("nome",)


admin.site.register(Aluno, AlunoAdmin)
