from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Author
from .forms import AuthorForm, RecipeForm, UserForm
from django.contrib.auth.decorators import login_required


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
        user_form = UserForm(request.POST, instance=request.user)
        author_form = AuthorForm(request.POST, instance=request.user.author)
        if user_form.is_valid() and author_form.is_valid():
            # breakpoint()
            author = author_form.save(commit=False)
            user_form.save()
            author_form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        user_form = UserForm(instance=request.user)
        author_form = AuthorForm(instance=request.user.author)
    return render(request, 'recipeapp/add_author.html',
                  {'user_form': user_form, 'author_form': author_form})

@login_required
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
