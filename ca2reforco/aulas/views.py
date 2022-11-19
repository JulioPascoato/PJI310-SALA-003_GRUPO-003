from django.shortcuts import render, redirect
from .models import Aula
from .forms import AulaForm

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


# Create your views here.


@login_required(login_url='login')
def aulas(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    if request.user.is_staff == True:
        aulas_all = Aula.objects.all()
        aulas = aulas_all.filter(nome__icontains=search_query)
    else:
        aulas_all = Aula.objects.order_by('-data_aula').filter(
            professor=request.user.professor)
        aulas = aulas_all.filter(
            nome__icontains=search_query)

    context = {
        'aulas': aulas,
        'search_query': search_query
    }

    return render(request, 'aulas/aulas.html', context)


@ login_required(login_url='login')
def aula(request, pk):
    aulaObj = Aula.objects.get(id=pk)
    return render(request, 'aulas/aula-individual.html', {'aula': aulaObj})


@ staff_member_required(login_url='login')
def novaAula(request):
    form = AulaForm()
    context = {'form': form}

    if request.method == "POST":
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

            messages.success(request, 'Aula nova criada com sucesso!')

            return redirect('aulas')
        else:
            messages.error(request, 'Ocorreu um erro ao criar a conta!')

    return render(request, 'aulas/aula_form.html', context)
