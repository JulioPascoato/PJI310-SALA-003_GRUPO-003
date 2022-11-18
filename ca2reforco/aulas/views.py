from django.shortcuts import render
from .models import Aula
from .forms import AulaForm

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def aulas(request):

    aulas = Aula.objects.order_by('-data_aula').filter(
        professor=request.user.professor)
    context = {
        'aulas': aulas
    }

    return render(request, 'aulas/aulas.html', context)


@login_required(login_url='login')
def aula(request, pk):
    aulaObj = Aula.objects.get(id=pk)
    return render(request, 'aulas/aula-individual.html', {'aula': aulaObj})


def novaAula(request):
    form = AulaForm()
    context = {'form': form}
    return render(request, 'aulas/aula_form.html', context)
