from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Author
from .forms import AuthorForm, RecipeForm


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
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            # breakpoint()
            author = form.save(commit=False)
            author.name = form.cleaned_data['name']
            author.bio = form.cleaned_data['bio']
            author.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, 'recipeapp/add_author.html', {'form': form})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
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
        form = RecipeForm()
    return render(request, 'recipeapp/add_recipe.html', {'form': form})
