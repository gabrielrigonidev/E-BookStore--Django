from . import views
from django.urls import path

urlpatterns = [
    path('', views.appBook, name="appBook"),
    path('cadastro/', views.cadastrar_user, name='cadastrar_user'),
    path('biblioteca/', views.cadastrar_livro, name='cadastrar_livro'),
    path('contato/', views.contato, name='contato'),
    path('livros/', views.exibir_livros, name='exibir_livros'),
    path('usuarios/', views.exibir_users, name='exibir_users'),
    path('login/', views.form_login, name='form_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editar_usuario/<int:id_usuario>', views.editar_usuario, name='editar_usuario'),
    path('excluir_usuario/<int:id_usuario>', views.excluir_usuario, name='excluir_usuario'),
    path('add-foto/', views.add_foto, name='add_foto'),
    path('galeria/', views.galeria, name='galeria'),
]