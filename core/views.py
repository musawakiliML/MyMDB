from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from core.models import Movie
# Create your views here.

class MovieList(ListView):
    model = Movie
    template_name = 'core/movie_list.html'
    context_object_name = 'movie_list'

class HomePageView(TemplateView):
    template_name = 'core/home.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'core/movie_detail.html'
    context_object_name = 'movie_detail'