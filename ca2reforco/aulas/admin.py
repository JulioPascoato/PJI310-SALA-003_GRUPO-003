from django.contrib import admin
from .models import Aula, Pacote, Sala
from rangefilter.filters import DateTimeRangeFilter, DateRangeFilter


class AulaAdmin(admin.ModelAdmin):
    list_display = ("nome", "professor", "data_aula", "sala")
    list_filter = ("professor", ("data_aula", DateRangeFilter), "sala")


# Register your models here.
admin.site.register(Aula, AulaAdmin)
admin.site.register(Pacote)
admin.site.register(Sala)
