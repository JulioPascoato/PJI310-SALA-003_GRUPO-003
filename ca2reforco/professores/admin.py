from django.contrib import admin
from .models import Professor, Habilidade


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "celular", "endereco")
    list_filter = ("nome",)


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Habilidade)
