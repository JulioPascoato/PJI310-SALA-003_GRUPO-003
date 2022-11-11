from django.urls import path
from . import views

urlpatterns = [
    path('', views.professores ,name="professores"),
    path('professor/<str:pk>', views.professor ,name="professor"),
]