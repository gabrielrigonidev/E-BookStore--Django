from . import views
from django.urls import path

urlpatterns = [
    path('', views.appBook, name="appBook"),
    path('cadastro/', views.cadastrar_user, name='cadastrar_user'),
    path('biblioteca/', views.cadastrar_livro, name='cadastrar_livro'),
    path('usuarios/', views.exibir_users, name='exibir_users'),
    path('login/', views.form_login, name='form_login'),
    path('dashboard/', views.dashboard, name='dashboard')
]