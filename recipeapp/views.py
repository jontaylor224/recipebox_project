from django.shortcuts import render, get_object_or_404
from .models import Recipe, Author


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
