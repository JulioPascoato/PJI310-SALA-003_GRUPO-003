from django.urls import path

from . import views

urlpatterns = [
    path('', views.aulas ,name="aulas"),
    path('aula/<str:pk>', views.aula ,name="aula"),
]