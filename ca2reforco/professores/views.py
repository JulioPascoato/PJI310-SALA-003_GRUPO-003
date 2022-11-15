from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.contrib import messages
from .models import Professor

from .forms import CustomUserCreationForm, ProfessorForm, HabilidadeForm

from django.contrib.auth.decorators import login_required
# Create your views here.


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('professores')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Usuário não existe')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('professores')
        else:
            messages.error(request, 'Usuário e/ou senha inválido(s)')

    return render(request, 'professores/login_register.html')


def logoutUser(request):
    logout(request)
    messages.warning(request, 'Encerrando a sessão do usuário')
    return redirect('login')


def professores(request):
    professores = Professor.objects.all()
    content = {
        'professores': professores
    }
    return render(request, 'professores/profiles.html', content)


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Sua nova conta foi criada com sucesso!')

            login(request, user)
            return redirect('edit-account')
        else:
            messages.error(request, 'Ocorreu um erro ao criar a conta!')

    context = {
        'page': page,
        'form': form

    }

    return render(request, 'professores/login_register.html', context)


def professor(request, pk):
    professor = Professor.objects.get(id=pk)

    topSkills = professor.habilidade_set.exclude(descricao__exact="")
    otherSkills = professor.habilidade_set.filter(descricao="")
    content = {
        'professor': professor,
        'topSkills': topSkills,
        'otherSkills': otherSkills,
    }
    return render(request, 'professores/profile.html', content)


@login_required(login_url='login')
def userAccount(request):

    profile = request.user.professor

    context = {'professor': profile}
    return render(request, 'professores/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.professor

    form = ProfessorForm(instance=profile)

    if request.method == "POST":
        form = ProfessorForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'professores/profile_form.html', context)


@login_required(login_url='login')
def createSkill(request):

    profile = request.user.professor
    print(profile)
    form = HabilidadeForm()

    if request.method == 'POST':

        form = HabilidadeForm(request.POST)

        if form.is_valid():
            habilidade = form.save(commit=False)
            habilidade.professor = profile
            # habilidade.save()

            print(habilidade.professor)

            return redirect('account')

    context = {'form': form}
    return render(request, 'professores/skill_form.html', context)
