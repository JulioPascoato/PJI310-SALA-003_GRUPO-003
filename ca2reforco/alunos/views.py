from django.shortcuts import render
from .models import Aluno

from django.db.models import Q

# Create your views here.


def alunos(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    alunos = Aluno.objects.distinct().filter(
        Q(nome__icontains=search_query) |
        Q(perfil__icontains=search_query) |
        Q(serie__icontains=search_query) |
        Q(colegio__icontains=search_query))

    content = {
        'alunos': alunos,
        'search_query': search_query
    }

    return render(request, 'alunos/alunos.html', content)


def aluno(request, pk):
    aluno = Aluno.objects.get(id=pk)

    content = {
        'aluno': aluno,

    }
    return render(request, 'alunos/profile.html', content)
