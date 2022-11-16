from django.shortcuts import render
from professores.models import Professor

# Create your views here.


def professores(request):
    professores = Professor.objects.all()
    content = {
        'professores': professores
    }
    return render(request, 'alunos/alunos.html', content)
