from django import forms
from django.forms import ModelForm
from .models import Postagem, Professor, Cadeira, Projeto, Educacao, Certificacao, ProjetoHobby


class PostForm(ModelForm):
    class Meta:
        model = Postagem
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do post'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do post'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Link do post', 'autocomplete': 'off'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor deste post'}),
        }

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
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome do docente', 'required': 'true'})
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'nome': 'Nome do docente'
        }


class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome da cadeira', 'required': 'true'}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Descreva a cadeira', 'required': 'true'}),
            'imagem': forms.FileInput(
                attrs={'class': 'form-control', 'required': 'true'}),
            'docente_teorica': forms.Select(
                choices=Professor.objects.all().order_by('nome'),
                attrs={'class': 'form-control', 'required': 'true'}),
            'docente_pratica': forms.Select(
                choices=Professor.objects.all().order_by('nome'),
                attrs={'class': 'form-control', 'required': 'true'}),
            'ano': forms.NumberInput(
                attrs={'class': 'form-control', 'min': '1', 'max': '3',
                       'placeholder': 'Ano letivo', 'required': 'true'}),
            'semestre': forms.NumberInput(
                attrs={'class': 'form-control', 'min': '1', 'max': '2',
                       'placeholder': 'Semestre', 'required': 'true'}),
            'ects': forms.NumberInput(
                attrs={'class': 'form-control', 'min': '4', 'max': '6',
                       'placeholder': 'Créditos', 'required': 'true'}),
        }

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
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Título do projeto', 'required': 'true'}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Descreva o projeto', 'required': 'true'}),
            'imagem': forms.FileInput(
                attrs={'class': 'form-control', 'required': 'true'}),
            'cadeira': forms.Select(
                choices=Cadeira.objects.all().order_by('nome'),
                attrs={'class': 'form-control', 'required': 'true'}),
            'link': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Link do projeto', 'autocomplete': 'off'}),
        }

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
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Título do projeto', 'required': 'true'}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Descreva o projeto', 'required': 'true'}),
            'imagem': forms.FileInput(
                attrs={'class': 'form-control', 'required': 'true'}),
            'online': forms.CheckboxInput(attrs={'style': 'margin-left: 10px;'}),
            'data': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Data da certificação',
                       'required': 'true'}),
            'link': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Link do projeto', 'autocomplete': 'off'}),
        }

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
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome do estabelecimento', 'required': 'true'}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Descreva esta etapa', 'required': 'true'}),
            'imagem': forms.FileInput(
                attrs={'class': 'form-control', 'required': 'true'}),
            'anos': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '2016 - 2019', 'max-length': '11',
                       'required': 'true'}),
            'certificacaoNivel': forms.NumberInput(
                attrs={'class': 'form-control', 'min': '1', 'max': '8',
                       'placeholder': 'Nível de certificação', 'required': 'true'}),
            'link': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Link do estabelecimento', 'autocomplete': 'off'}),
        }

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
        widgets = {
            'local': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome do estabelecimento', 'required': 'true'}),
            'tipo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Tipo de certificação', 'required': 'true'}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Descreva esta certificação', 'required': 'true'}),
            'imagem': forms.FileInput(
                attrs={'class': 'form-control', 'required': 'true'}),
            'data': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Data da certificação',
                       'required': 'true'}),
            'link': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Link para mais detalhes', 'autocomplete': 'off'}),
        }

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
