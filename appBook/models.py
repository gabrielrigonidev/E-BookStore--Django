from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='usuarios/')

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    paginas = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='livros/')

class Foto(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='imagens/')