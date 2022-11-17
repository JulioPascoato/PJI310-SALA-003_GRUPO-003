from django.shortcuts import render
from .models import Aluno

# Create your views here.


def alunos(request):
    alunos = Aluno.objects.all()
    content = {
        'alunos': alunos
    }
    return render(request, 'alunos/alunos.html', content)


def aluno(request, pk):
    aluno = Aluno.objects.get(id=pk)

    content = {
        'aluno': aluno,

    }
    return render(request, 'alunos/profile.html', content)
