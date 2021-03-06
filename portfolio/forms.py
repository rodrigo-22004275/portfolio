from django import forms
from django.forms import ModelForm
from .models import Postagem, Professor, Cadeira, Projeto, Educacao, Certificacao, ProjetoHobby, Tecnologia, \
    Laboratorio, Noticia, Comentario, TFC


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


class TFCForm(ModelForm):
    class Meta:
        model = TFC
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Título do projeto', 'required': 'true'}),
            'resumo': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Resumo do projeto', 'required': 'true'}),
            'imagem': forms.FileInput(
                attrs={'class': 'form-control', 'required': 'true'}),
            'aluno': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome do aluno', 'required': 'true'}),
            'orientador': forms.Select(
                choices=Professor.objects.all().order_by('nome'),
                attrs={'class': 'form-control', 'required': 'true'}),
            'video': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'ID do video do projeto', 'autocomplete': 'off'}),
            'relatorio': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Link do relatório', 'autocomplete': 'off', 'required': 'true'}),
            'link': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Link do projeto', 'autocomplete': 'off', 'required': 'true'}),
            'data': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Data do projeto', 'required': 'true'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'resumo': 'Resumo',
            'imagem': 'Imagem do projeto',
            'aluno': 'Nome do aluno',
            'orientador': 'Orientador',
            'video': 'Video',
            'relatorio': 'Relatório',
            'link': 'GitHub',
            'data': 'Data'
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


class TecnologiaForm(ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome da tecnologia', 'required': 'true'}),
            'acronimo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Acrónimo da tecnologia'}),
            'anoCriacao': forms.NumberInput(
                attrs={'class': 'form-control', 'max-length': '4',
                       'placeholder': 'Ano de criação', 'required': 'true'}),
            'criador': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Criador da tecnologia', 'required': 'true'}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Descreva esta tecnologia', 'required': 'true'}),
            'presentationlayer': forms.Select(
                choices=[('Back-end', 'Back-end'), ('Front-end', 'Front-end'),
                         ('Desktop', 'Desktop'), ('Mobile', 'Mobile'), ('Web', 'Web'), ('Embedded', 'Embedded')],
                attrs={'class': 'form-control', 'required': 'true'}),
            'logotipo': forms.FileInput(
                attrs={'class': 'form-control', 'required': 'true'}),
            'usado': forms.CheckboxInput(attrs={'style': 'margin-left: 10px;'}),
            'formaUso': forms.TextInput(
                attrs={'class': 'form-control'}),
            'link': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Link para mais detalhes', 'autocomplete': 'off'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'acronimo': 'Acrónimo',
            'descricao': 'Descrição',
            'data': 'Data da certificação',
            'anoCriacao': 'Ano de criação',
            'presentationlayer': 'Layer de apresentação',
            'usado': 'É utilizada neste website?',
            'formaUso': 'De que forma foi utilizada neste website?',
            'link': 'Website oficial'
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'formaUso': 'Apenas preencha este campo se esta tecnologia foi utilizada neste website',
            'link': 'Este campo é opcional'
        }


class LaboratorioForm(ModelForm):
    class Meta:
        model = Laboratorio
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Título do laboratório', 'required': 'true'}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Descrição do laboratório', 'required': 'true'}),
            'link': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Link para laboratório',
                       'autocomplete': 'off', 'required': 'true'})
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'link': 'Link para Laboratório'
        }


class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Título da notícia', 'required': 'true'}),
            'descricao': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Descrição da notícia', 'required': 'true'}),
            'link': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Link para a notícia',
                       'autocomplete': 'off', 'required': 'true'}),
            'imagem': forms.FileInput(
                attrs={'class': 'form-control', 'required': 'true'})
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'imagem': 'Imagem de apresentação',
            'link': 'Link para notícia'
        }


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do comentário', 'required': 'true'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control',
                                               'placeholder': 'O que tem a dizer sobre este website?', 'required': 'true'}),
            'avaliacao': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '10',
                                                  'placeholder': 'Avalie de 1 a 10 estrelas', 'required': 'true'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor deste comentário', 'required': 'true'}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'A sua opinião',
            'imagem': 'Imagem de perfil',
            'avaliacao': 'A sua avaliação',
            'autor': 'O seu nome',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'link': 'Este campo é opcional',
        }
