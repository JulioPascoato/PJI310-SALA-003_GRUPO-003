from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunos, name="alunos"),
    path('aluno/<str:pk>', views.aluno, name="aluno"),
]
