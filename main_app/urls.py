from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('posts/', views.Blog_Post_List.as_view(), name='blogpost_list'),
    path('posts/new/', views.Post_Create.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.Post_Detail.as_view(), name='post_detail'),

]