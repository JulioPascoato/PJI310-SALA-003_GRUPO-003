from django.contrib import admin
from .models import Aula, Pacote, Sala
from rangefilter.filters import DateTimeRangeFilter, DateRangeFilter


class AulaAdmin(admin.ModelAdmin):
    list_display = ("nome", "professor", "aluno", "data_aula", "sala")
    list_filter = ("professor", ("data_aula", DateRangeFilter), "sala")


class PacoteAdmin(admin.ModelAdmin):
    list_display = ("tipo", "duracao_aula", "valor")
    list_filter = ("tipo", "duracao_aula", "valor")


# Register your models here.
admin.site.register(Aula, AulaAdmin)
admin.site.register(Pacote, PacoteAdmin)
admin.site.register(Sala)
