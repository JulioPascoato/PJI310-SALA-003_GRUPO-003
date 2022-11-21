import django_filters
from django_filters import DateFilter, DateFromToRangeFilter

from .models import Aula


class AulaFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='data_aula', lookup_expr='gte')
    end_date = DateFilter(field_name='data_aula', lookup_expr='lte')

    class Meta:
        model = Aula
        fields = ['aluno']
        exclude = ['id', 'pacote', 'created', 'data_aula', 'nome', 'conteudo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.filters["aluno"].field.widget.attrs.update(
            {"class": "form-control"})

        self.filters["start_date"].field.widget.attrs.update(
            {"class": "form-control"})

        self.filters["end_date"].field.widget.attrs.update(
            {"class": "form-control"})
