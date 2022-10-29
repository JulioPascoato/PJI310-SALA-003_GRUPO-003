from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
projectsList = [

    {'id': '1', 'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'},

    {'id': '2', 'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'},

    {'id': '3', 'title': 'Social Network',
        'description': 'An open source project built by the community'}

]


def aulas(request):
   
    context = {
        'projects': projectsList
    }

    return render(request, 'aulas/aulas.html', context)


def aula(request, pk):
    aulaObj = None
    for i in projectsList:
        if i['id'] == pk:
            aulaObj = i

    return render(request, 'aulas/aula-individual.html', {'aula': aulaObj})
