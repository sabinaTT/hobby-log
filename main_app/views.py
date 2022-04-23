from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    # def get(self, request):
    #     return HttpResponse('HobbyLog Home')

class About(TemplateView):
    template_name = 'about.html'
    # def get(self, request):
    #     return HttpResponse('HobbyLog About')

class Post:
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body

posts = [
    Post('A new hobby I want to earn is gardening!', 'Sabina', 'One morning, I woke up...'),
    Post('Gardening 101', 'Sabina', 'It is always difficult to figure out where to start! Here are some tips from my own experience')
]

class Blog_Post_List(TemplateView):
    template_name  = 'blogpost_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = posts
        return context