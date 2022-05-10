import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse

from portfolio.forms import PostForm
from portfolio.models import Postagem, PontuacaoQuizz

from matplotlib import pyplot as plt


def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }
    return render(request, 'portfolio/home.html', context)


def uni_page_view(request):
    cursos = [
        {
            "nome": "Fundamentos de Física",
            "semestre": "1º ano 1º Semestre",
            "ects": "6",
            "professor": "Cristiane"
        },
        {
            "nome": "Fundamentos de Programação",
            "semestre": "1º ano 1º Semestre",
            "ects": "6",
            "professor": "Pedro Alves"
        },
        {
            "nome": "Matemática Discreta",
            "semestre": "1º ano 1º Semestre",
            "ects": "6",
            "professor": "Teresa Almada"
        },
        {
            "nome": "Matemática I",
            "semestre": "1º ano 1º Semestre",
            "ects": "6",
            "professor": "André Fonseca"
        },
        {
            "nome": "Sistemas Digitais",
            "semestre": "1º ano 1º Semestre",
            "ects": "6",
            "professor": "João Pedro Carvalho"
        },
        {
            "nome": "Álgebra Linear",
            "semestre": "1º ano 2º Semestre",
            "ects": "5",
            "professor": "Teresa Almada"
        },
        {
            "nome": "Algoritmia e Estruturas de Dados",
            "semestre": "1º ano 2º Semestre",
            "ects": "6",
            "professor": "Pedro Alves"
        },
        {
            "nome": "Arquitetura de Computadores",
            "semestre": "1º ano 2º Semestre",
            "ects": "5",
            "professor": "Pedro Serra"
        },
        {
            "nome": "Competências Comportamentais",
            "semestre": "1º ano 2º Semestre",
            "ects": "4",
            "professor": "Diogo Morais"
        },
        {
            "nome": "Linguagens de Programação I",
            "semestre": "1º ano 2º Semestre",
            "ects": "5",
            "professor": "Pedro Serra"
        },
        {
            "nome": "Matemática II",
            "semestre": "1º ano 2º Semestre",
            "ects": "5",
            "professor": "André Fonseca"
        },
        {
            "nome": "Arquiteturas Avançadas de Computadores",
            "semestre": "2º ano 1º Semestre",
            "ects": "6",
            "professor": "Pedro Serra"
        },
        {
            "nome": "Bases de Dados",
            "semestre": "2º ano 1º Semestre",
            "ects": "6",
            "professor": "Rui Ribeiro"
        },
        {
            "nome": "Linguagens de Programação II",
            "semestre": "2º ano 1º Semestre",
            "ects": "6",
            "professor": "Pedro Alves"
        },
        {
            "nome": "Sinais e Sistemas",
            "semestre": "2º ano 1º Semestre",
            "ects": "6",
            "professor": "João Canto"
        },
        {
            "nome": "Sistemas Operativos",
            "semestre": "2º ano 1º Semestre",
            "ects": "6",
            "professor": "Naercio"
        }
    ]

    context = {
        'cursos': cursos,
    }
    return render(request, 'portfolio/licenciatura.html', context)


def projects_page_view(request):
    projetos = [
        {
            "titulo": "Exemplo 1",
            "semestre": "1º ano 1º semestre",
            "cadeira": "LP1",
            "imagem": "programming.jpg"
        },
        {
            "titulo": "Exemplo 2",
            "semestre": "1º ano 1º semestre",
            "cadeira": "LP1",
            "imagem": "programming.jpg"
        },
        {
            "titulo": "Exemplo 3",
            "semestre": "1º ano 1º semestre",
            "cadeira": "LP1",
            "imagem": "programming.jpg"
        }
    ]

    context = {
        'projetos': projetos,
    }

    return render(request, 'portfolio/projects.html', context)


def contact_page_view(request):
    return render(request, 'portfolio/contact.html')


def blog_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {
        'posts': Postagem.objects.all(),
        'form': form,
        'agora': datetime.datetime.now(),
    }
    return render(request, 'portfolio/blog.html', context)


def quizz_page_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
        desenha_grafico_resultados()

    return render(request, 'portfolio/quizz.html')


def pontuacao_quizz(request):
    pontuacao = 0
    if request.POST['extensao'] == ".html":
        pontuacao += 2

    if request.POST['tecnologias'] == "py":
        pontuacao += 2

    if request.POST['pySemPontoVirgula'] == "true":
        pontuacao += 2

    if request.POST['djangoIsWordpress'] == "false":
        pontuacao += 2

    if request.POST['djangoDB'] == "true":
        pontuacao += 2

    return pontuacao


def desenha_grafico_resultados():
    participantes = sorted(PontuacaoQuizz.objects.all(), key=lambda t: t.pontuacao, reverse=True)

    nomes = []
    pontuacoes = []

    for pt in participantes:
        nomes.append(pt.nome)
        pontuacoes.append(pt.pontuacao)

    plt.barh(nomes, pontuacoes)
    plt.savefig("portfolio/static/portfolio/images/grafico.png", bbox_inches='tight')
