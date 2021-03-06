import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from portfolio.forms import PostForm, ProfessorForm, CadeiraForm, ProjetoForm, EducacaoForm, CertificacaoForm, \
    ProjetoHobbyForm, TecnologiaForm, LaboratorioForm, NoticiaForm, ComentarioForm, TFCForm
from portfolio.models import Postagem, PontuacaoQuizz, Professor, Cadeira, Projeto, Mensagem, Educacao, Certificacao, \
    ProjetoHobby, Tecnologia, Laboratorio, Noticia, Comentario, TFC

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
        'escolas': Educacao.objects.all().order_by('-certificacaoNivel'),
        'certificacao': Certificacao.objects.all().order_by('-data', 'tipo')
    }
    return render(request, 'portfolio/sobremim.html', context)


def projects_page_view(request):
    context = {
        'projetos': Projeto.objects.all().order_by('-cadeira'),
        'projetosHobby': ProjetoHobby.objects.all().order_by('-data'),
        'TFCs': TFC.objects.all().order_by('-data')
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
    context = {
        'posts': Postagem.objects.all().order_by('-data'),
        'agora': datetime.datetime.now(),
    }
    return render(request, 'portfolio/blog.html', context)


def web_page_view(request):
    if request.method == 'POST' and request.user.is_authenticated:
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
        desenha_grafico_resultados()

    context = {
        'tecnologias': Tecnologia.objects.all().order_by('presentationlayer', '-anoCriacao'),
        'labs': Laboratorio.objects.all().order_by('titulo'),
        'noticias': Noticia.objects.all().order_by('titulo'),
        'techUsada': Tecnologia.objects.all().filter(usado=True).order_by('presentationlayer', '-anoCriacao'),
        'comentarios': Comentario.objects.all().order_by('-data')
    }

    return render(request, 'portfolio/web.html', context)


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
    participantes = sorted(PontuacaoQuizz.objects.all().order_by('-pontuacao'), key=lambda x: x.pontuacao)

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
        link = 'projects'
    elif tipo == 'hobby':
        form = ProjetoHobbyForm(request.POST or None, request.FILES or None)
        link = 'projects'
    elif tipo == 'TFC':
        form = TFCForm(request.POST or None, request.FILES or None)
        link = 'projects'
    elif tipo == 'educacao':
        form = EducacaoForm(request.POST or None, request.FILES or None)
        link = 'aboutme'
    elif tipo == 'certificacao':
        form = CertificacaoForm(request.POST or None, request.FILES or None)
        link = 'aboutme'
    elif tipo == 'tecnologia':
        form = TecnologiaForm(request.POST or None, request.FILES or None)
        link = 'web'
    elif tipo == 'laboratorio':
        form = LaboratorioForm(request.POST or None, request.FILES or None)
        link = 'web'
    elif tipo == 'noticia':
        form = NoticiaForm(request.POST or None, request.FILES or None)
        link = 'web'
    elif tipo == 'comentario':
        form = ComentarioForm(request.POST or None, request.FILES or None)
        link = 'web'
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
        link = 'projects'
    elif tipo == 'hobby':
        objeto = ProjetoHobby.objects.get(id=tipo_id)
        form = ProjetoHobbyForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'projects'
    elif tipo == 'TFC':
        objeto = TFC.objects.get(id=tipo_id)
        form = TFCForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'projects'
    elif tipo == 'educacao':
        objeto = Educacao.objects.get(id=tipo_id)
        form = EducacaoForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'aboutme'
    elif tipo == 'certificacao':
        objeto = Certificacao.objects.get(id=tipo_id)
        form = CertificacaoForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'aboutme'
    elif tipo == 'tecnologia':
        objeto = Tecnologia.objects.get(id=tipo_id)
        form = TecnologiaForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'web'
    elif tipo == 'laboratorio':
        objeto = Laboratorio.objects.get(id=tipo_id)
        form = LaboratorioForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'web'
    elif tipo == 'noticia':
        objeto = Noticia.objects.get(id=tipo_id)
        form = NoticiaForm(request.POST or None, request.FILES or None, instance=objeto)
        link = 'web'
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
        return HttpResponseRedirect(reverse('portfolio:blog'))
    elif tipo == 'cadeira':
        Cadeira.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))
    elif tipo == 'projeto':
        Projeto.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:projects'))
    elif tipo == 'hobby':
        ProjetoHobby.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:projects'))
    elif tipo == 'TFC':
        TFC.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:projects'))
    elif tipo == 'educacao':
        Educacao.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))
    elif tipo == 'certificacao':
        Certificacao.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:aboutme'))
    elif tipo == 'tecnologia':
        Tecnologia.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:web'))
    elif tipo == 'laboratorio':
        Laboratorio.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:web'))
    elif tipo == 'noticia':
        Noticia.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:web'))
    elif tipo == 'comentario':
        Comentario.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:web'))
    elif tipo == 'docentes':
        Professor.objects.get(id=tipo_id).delete()
        return HttpResponseRedirect(reverse('portfolio:docentes'))
    else:
        return HttpResponseRedirect(reverse('portfolio:404'))


def comentar_view(request):
    form = ComentarioForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse(f'portfolio:web'))

    context = {
        'tipo': 'nada',
        'form': form
    }
    return render(request, 'portfolio/novo.html', context)


def view_404(request):
    return render(request, 'portfolio/404.html')
