from django.contrib import admin

# Register your models here.
from .models import Postagem, PontuacaoQuizz, Cadeira, Projeto, Professor, Mensagem, Educacao, Certificacao

admin.site.register(Postagem)
admin.site.register(PontuacaoQuizz)
admin.site.register(Professor)
admin.site.register(Cadeira)
admin.site.register(Projeto)
admin.site.register(Educacao)
admin.site.register(Certificacao)
admin.site.register(Mensagem)
