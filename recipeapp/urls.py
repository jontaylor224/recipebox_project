from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('addauthor/', views.add_author, name='add_author'),
    path('addrecipe/', views.add_recipe, name='add_recipe'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
