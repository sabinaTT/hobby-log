from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'
    # def get(self, request):
    #     return HttpResponse('HobbyLog Home')

class About(TemplateView):
    template_name = 'about.html'
    # def get(self, request):
    #     return HttpResponse('HobbyLog About')

class Blog_Post_List(TemplateView):
    template_name  = 'blogpost_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.request.GET.get('post')
        if post != None:
            context['posts'] = Post.objects.filter(post__icontains=post)
        else:
            context['posts'] = Post.objects.all()
        return context

class Post_Create(CreateView):
    model = Post
    fields = ['post_title', 'post', 'img']
    template_name = 'post_create.html'
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class Post_Detail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class Post_Update(UpdateView):
    model = Post
    fields = ['post_title', 'post', 'img']
    template_name = 'post_update.html'
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})