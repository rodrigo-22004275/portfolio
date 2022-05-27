from django.conf.urls.static import static
from django.shortcuts import render
from django.urls import path

from config import settings
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('blog', views.blog_page_view, name='blog'),
    path('projects', views.projects_page_view, name='projects'),
    path('licenciatura', views.uni_page_view, name='licenciatura'),
    path('adicionarDocente', views.form_docente_view, name='docentes'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('contact', views.contact_page_view, name='contact'),
    path('login', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout')
]
