from django.shortcuts import (
    render, get_object_or_404, redirect, HttpResponseRedirect)
from django.contrib.auth.models import User
from .models import Recipe, Author
from .forms import AuthorForm, AdminRecipeForm, UserRecipeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipeapp/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipeapp/recipe_detail.html', {'recipe': recipe})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    recipes = Recipe.objects.filter(author_id=author.id)
    return render(request,
                  'recipeapp/author_detail.html',
                  {'author': author, 'recipes': recipes})


def add_author(request):
    if not request.user.is_staff:
        return HTTPResponseRedirect('/')
    else:
        if request.method == "POST":
            author_form = AuthorForm(request.POST)
            if author_form.is_valid():
                author_data = author_form.cleaned_data
                password1 = author_data.get("password1")
                password2 = author_data.get("password2")

                if (password1 == password2):
                    new_user = User.objects.create_user(
                        username=author_data.get("username"),
                        password=password2,
                    )
                    author = Author.objects.create(
                        user=new_user,
                        bio=author_data.get("bio")
                    )
                    return redirect('author_detail', pk=author.pk)
        else:
            author_form = AuthorForm()
    return render(request, 'recipeapp/add_author.html',
                  {'author_form': author_form})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        if request.user.is_staff:
            form = AdminRecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                recipe = Recipe.objects.create(
                    title=data.get('title'),
                    author=data.get('author'),
                    description=data.get('description'),
                    time_required=data.get('time_required'),
                    instructions=data.get('instructions')
                )
                return redirect('recipe_detail', pk=recipe.pk)
        else:
            if request.method == 'POST':
                form = UserRecipeForm(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    recipe = Recipe.objects.create(
                        title=data.get('title'),
                        author=request.user.author,
                        description=data.get('description'),
                        time_required=data.get('time_required'),
                        instructions=data.get('instructions')
                    )
                    return redirect('recipe_detail', pk=recipe.pk)
    else:
        if request.user.is_staff:
            form = AdminRecipeForm()
        else:
            form = UserRecipeForm()
    return render(request, 'recipeapp/add_recipe.html', {'form': form})


def logout_view(request):
    logout(request)
