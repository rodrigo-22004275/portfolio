from django.shortcuts import render
from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('blog', views.blog_page_view, name='blog'),
    path('projects', views.projects_page_view, name='projects'),
    path('licenciatura', views.uni_page_view, name='licenciatura'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('contact', views.contact_page_view, name='contact')
]
