import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from portfolio.forms import PostForm, ProfessorForm
from portfolio.models import Postagem, PontuacaoQuizz, Professor, Cadeira, Projeto, Mensagem

from matplotlib import pyplot as plt


def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas.'
            })

    return render(request, 'portfolio/login.html')


def view_logout(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'Foi desconetado.'
    })


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
    if request.method == 'POST':
        Cadeira(nome=request.POST['nome'],
                ano=request.POST['ano'],
                semestre=request.POST['semestre'],
                ects=request.POST['ects'],
                descricao=request.POST['descricao'],
                imagem=request.FILES['imagem'],
                docente_teorica=Professor.objects.get(nome=request.POST['docente_teorica']),
                docente_pratica=Professor.objects.get(nome=request.POST['docente_pratica'])).save()

    context = {
        'cadeiras': Cadeira.objects.all().order_by('ano', 'semestre', 'nome', 'ects'),
        'docentes': Professor.objects.all().order_by('nome')
    }
    return render(request, 'portfolio/licenciatura.html', context)


def projects_page_view(request):
    if request.method == 'POST' and request.user.is_authenticated:
        Projeto(titulo=request.POST['titulo'],
                descricao=request.POST['descricao'],
                cadeira=Cadeira.objects.get(nome=request.POST['cadeira']),
                imagem=request.FILES['imagem'],
                link=request.POST['link']).save()

    context = {
        'projetos': Projeto.objects.all()
    }

    return render(request, 'portfolio/projects.html', context)


def contact_page_view(request):
    if request.method == 'POST':
        Mensagem(nome=request.POST['nome'],
                 mensagem=request.POST['mensagem'],
                 email=request.POST['email'],
                 data=datetime.datetime.now()).save()

    return render(request, 'portfolio/contact.html')


def blog_page_view(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {
        'posts': Postagem.objects.all().order_by('-data'),
        'form': form,
        'agora': datetime.datetime.now(),
    }
    return render(request, 'portfolio/blog.html', context)


def quizz_page_view(request):
    if request.method == 'POST' and request.user.is_authenticated:
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


@login_required
def form_docente_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = ProfessorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {
        'form': form,
        'docentes': Professor.objects.all().order_by('nome')
    }
    return render(request, 'portfolio/formDocente.html', context)
