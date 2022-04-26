from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('posts/', views.Blog_Post_List.as_view(), name='blogpost_list'),
    path('posts/new/', views.Post_Create.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.Post_Detail.as_view(), name='post_detail'),
    path('posts/<int:pk>/update', views.Post_Update.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', views.Post_Delete.as_view(), name='post_delete'),
    path('user/<username>', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/signup/', views.signup_view, name='signup'),
]