from django.shortcuts import render
from .models import Professor

# Create your views here.

def professores(request):
    professores = Professor.objects.all()
    content = {
        'professores' : professores
    }
    return render(request, 'professores/profiles.html', content)

def professor(request, pk):
    professor = Professor.objects.get(id=pk)

    topSkills = professor.habilidade_set.exclude(descricao__exact="")
    otherSkills = professor.habilidade_set.filter(descricao="")
    content = {
        'professor' : professor,
        'topSkills' : topSkills,
        'otherSkills' : otherSkills,
    }
    return render(request, 'professores/profile.html', content)

