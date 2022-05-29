from django.db import models

# Create your models here.
from config.settings import MEDIA_URL


def resolution_path(instance, filename):
    return MEDIA_URL


class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='blog/', blank=True)
    link = models.URLField(blank=True)
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=100)
    pontuacao = models.CharField(max_length=2)

    def __str__(self):
        return self.nome[:50]


class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome[:50]


class Cadeira(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='cadeiras/', blank=True)
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='docente_teorica')
    docente_pratica = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='docente_pratica')
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField(default=0)

    def __str__(self):
        return self.nome[:50]


class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True)
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo[:50]


class ProjetoHobby(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos_hobby/', blank=True)
    data = models.DateTimeField()
    link = models.URLField(blank=True)
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo[:50]


class Educacao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='educacao/', blank=True)
    anos = models.CharField(max_length=100)
    certificacaoNivel = models.IntegerField()
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome[:50]


class Certificacao(models.Model):
    local = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='certificacao/', blank=True)
    data = models.DateTimeField()
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.tipo[:50]


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    acronimo = models.CharField(max_length=100, null=True, blank=True)
    anoCriacao = models.CharField(max_length=4)
    criador = models.CharField(max_length=100)
    descricao = models.TextField()
    presentationlayer = models.CharField(max_length=100)
    logotipo = models.ImageField(upload_to='tecnologias/', blank=True)
    data = models.DateTimeField()
    usado = models.BooleanField(default=False)
    formaUso = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome[:50]


class Laboratorio(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.titulo[:50]


class Comentario(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    avaliacao = models.CharField(max_length=2)
    imagem = models.ImageField(upload_to='comentarios/', blank=True)
    link = models.URLField(blank=True)
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]


class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome[:50]
