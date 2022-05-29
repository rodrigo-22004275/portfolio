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
    path('aboutme', views.about_me_view, name='aboutme'),
    path('adicionarDocente', views.form_docente_view, name='docentes'),
    path('web', views.web_page_view, name='web'),
    path('contact', views.contact_page_view, name='contact'),
    path('novo/<str:tipo>', views.add_view, name='novo'),
    path('editar/<str:tipo>/<int:tipo_id>', views.edit_view, name='editar'),
    path('apagar/<str:tipo>/<int:tipo_id>', views.delete_view, name='apagar'),
    path('login', views.view_login, name='login'),
    path('logout', views.view_logout, name='logout'),
    path('404', views.view_404, name='404')
]
