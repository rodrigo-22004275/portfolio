from django import forms
from django.forms import ModelForm
from .models import Postagem, Professor


class PostForm(ModelForm):
    class Meta:
        model = Postagem
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título do post'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do post'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link do post', 'autocomplete': 'off'}),
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
