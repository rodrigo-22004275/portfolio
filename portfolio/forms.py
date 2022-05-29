from django import forms
from django.forms import ModelForm
from .models import Postagem, Professor, Cadeira, Projeto, Educacao, Certificacao, ProjetoHobby


class PostForm(ModelForm):
    class Meta:
        model = Postagem
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'imagem': 'Selecione imagem',
            'link': 'Link',
            'autor': 'Autor',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'link': 'Este campo é opcional',
        }


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome do docente'
        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome da cadeira',
            'descricao': 'Descreva a cadeira',
            'imagem': 'Imagem de apresentação',
            'docente_teorica': 'Docente da componente teórica',
            'docente_pratica': 'Docente da componente prática',
            'ano': 'Ano da cadeira',
            'semestre': 'Semestre',
            'ects': 'ECTs'
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'docente_teorica':
                'Falta algum docente? Poderá adicioná-lo <a href="docentes">aqui</a>',
            'docente_pratica':
                'Falta algum docente? Poderá adicioná-lo <a href="docentes">aqui</a>'
        }


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título do projeto',
            'descricao': 'Descreva este projeto',
            'imagem': 'Imagem de apresentação',
            'cadeira': 'Cadeira',
            'link': 'Link'
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'link': 'Este campo é opcional',
        }


class ProjetoHobbyForm(ModelForm):
    class Meta:
        model = ProjetoHobby
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título do projeto',
            'descricao': 'Descreva este projeto',
            'imagem': 'Imagem de apresentação',
            'data': 'Data de lançamento',
            'online': 'Projeto ainda ativo?',
            'link': 'Link'
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'link': 'Este campo é opcional',
        }


class EducacaoForm(ModelForm):
    class Meta:
        model = Educacao
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'imagem': 'Imagem de apresentação',
            'anos': 'Anos de estudo',
            'certificacaoNivel': 'Certificação',
            'link': 'Link'
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'link': 'Este campo é opcional'
        }


class CertificacaoForm(ModelForm):
    class Meta:
        model = Certificacao
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário


        # texto a exibir junto à janela de inserção
        labels = {
            'local': 'Estabelecimento',
            'tipo': 'Tipo de certificação',
            'descricao': 'Descrição',
            'imagem': 'Imagem de apresentação',
            'data': 'Data da certificação',
            'link': 'Link de detalhes'
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'link': 'Este campo é opcional'
        }
