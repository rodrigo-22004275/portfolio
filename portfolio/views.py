import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from portfolio.forms import PostForm, ProfessorForm, CadeiraForm, ProjetoForm, EducacaoForm
from portfolio.models import Postagem, PontuacaoQuizz, Professor, Cadeira, Projeto, Mensagem, Educacao

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


def about_me_view(request):
    context = {
        'cadeiras': Cadeira.objects.all().order_by('-ano', '-semestre', 'nome', '-ects'),
        'escolas': Educacao.objects.all().order_by('-certificacaoNivel')
    }
    return render(request, 'portfolio/sobremim.html', context)


def projects_page_view(request):
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
        return HttpResponseRedirect(reverse('portfolio:aboutme'))

    context = {
        'form': form,
        'docentes': Professor.objects.all().order_by('nome')
    }
    return render(request, 'portfolio/formDocente.html', context)


@login_required
def add_view(request, tipo):
    if tipo == 'post':
        form = PostForm(request.POST or None, request.FILES or None)
        link = 'blog'
    elif tipo == 'cadeira':
        form = CadeiraForm(request.POST or None, request.FILES or None)
        link = 'aboutme'
    elif tipo == 'projeto':
        form = ProjetoForm(request.POST or None, request.FILES or None)
        link = 'projetos'
    elif tipo == 'educacao':
        form = EducacaoForm(request.POST or None, request.FILES or None)
        link = 'aboutme'
    elif tipo == 'docentes':
        return HttpResponseRedirect(reverse('portfolio:docentes'))
    else:
        return HttpResponseRedirect(reverse('portfolio:404'))

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse(f'portfolio:{link}'))

    context = {
        'tipo': tipo.capitalize(),
        'form': form
    }
    return render(request, 'portfolio/novo.html', context)


@login_required
def edit_view(request, tipo, tipo_id):
    if tipo == 'post':
        objeto = Postagem.objects.get(id=tipo_id)
        form = PostForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'blog'
    elif tipo == 'cadeira':
        objeto = Cadeira.objects.get(id=tipo_id)
        form = CadeiraForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'aboutme'
    elif tipo == 'projeto':
        objeto = Projeto.objects.get(id=tipo_id)
        form = ProjetoForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'projetos'
    elif tipo == 'educacao':
        objeto = Educacao.objects.get(id=tipo_id)
        form = EducacaoForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'aboutme'
    elif tipo == 'docentes':
        return HttpResponseRedirect(reverse('portfolio:docentes'))
    else:
        return HttpResponseRedirect(reverse('portfolio:404'))

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse(f'portfolio:{link}'))

    context = {
        'tipo': tipo.capitalize(),
        'tipo_normal': tipo,
        'id': tipo_id,
        'form': form
    }
    return render(request, 'portfolio/edit.html', context)


@login_required
def delete_view(request, tipo, tipo_id):
    if tipo == 'post':
        Postagem.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse(f'portfolio:blog'))
    elif tipo == 'cadeira':
        Cadeira.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse(f'portfolio:aboutme'))
    elif tipo == 'projeto':
        Projeto.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse(f'portfolio:projetos'))
    elif tipo == 'educacao':
        Educacao.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse(f'portfolio:aboutme'))
    elif tipo == 'docentes':
        Professor.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse(f'portfolio:docentes'))
    else:
        return HttpResponseRedirect(reverse('portfolio:404'))


def view_404(request):
    return render(request, 'portfolio/404.html')