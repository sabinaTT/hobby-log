from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
    fields = '__all__'
    success_url = '/posts'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/posts')
    # def get_success_url(self):
    #     return reverse('post_detail', kwargs={'pk': self.object.pk})

class Post_Detail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class Post_Update(UpdateView):
    model = Post
    fields = ['post_title', 'post', 'img']
    template_name = 'post_update.html'
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class Post_Delete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url='/posts/'

def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'posts': posts})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('Greetings', user.username)
            return HttpsResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpsResponseRedirect('/posts')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpsResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return render(request, 'login.html', {'form': form})
            else:
                print('The username and/or password is incorrect.')
                return redner(request, 'login.html', {'form': form})
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})