from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),


    path('', views.professores, name="professores"),
    path('professor/<str:pk>', views.professor, name="professor"),
    path('account/', views.userAccount, name="account")
]
