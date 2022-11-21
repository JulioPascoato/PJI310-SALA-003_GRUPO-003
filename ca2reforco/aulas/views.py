from django.shortcuts import render, redirect
from .models import Aula
from .forms import AulaForm

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .filters import AulaFilter


# Create your views here.


@login_required(login_url='login')
def aulas(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    if request.user.is_staff == True:
        aulas = Aula.objects.all()
        myFilter = AulaFilter(request.GET, queryset=aulas)
        aulas = myFilter.qs
    else:
        aulas = Aula.objects.order_by('-data_aula').filter(
            professor=request.user.professor)

    myFilter = AulaFilter(request.GET, queryset=aulas)
    aulas = myFilter.qs

    context = {
        'aulas': aulas,
        'search_query': search_query,
        'myFilter': myFilter
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
