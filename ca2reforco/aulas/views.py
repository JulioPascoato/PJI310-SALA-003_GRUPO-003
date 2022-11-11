from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Aula
from .forms import AulaForm
# Create your views here.


def aulas(request):

    aulas = Aula.objects.all()
    context = {
        'aulas': aulas
    }

    return render(request, 'aulas/aulas.html', context)


def aula(request, pk):
    aulaObj = Aula.objects.get(id=pk)
    return render(request, 'aulas/aula-individual.html', {'aula': aulaObj})


def novaAula(request):
    form = AulaForm()
    context = {'form': form}
    return render(request, 'aulas/aula_form.html', context)
