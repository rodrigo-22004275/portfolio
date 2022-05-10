from django.contrib import admin

# Register your models here.
from .models import Postagem, PontuacaoQuizz

admin.site.register(Postagem)
admin.site.register(PontuacaoQuizz)
