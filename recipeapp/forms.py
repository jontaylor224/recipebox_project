from django import forms
from .models import Recipe, Author


class AuthorForm(forms.ModelForm):
    class Meta():
        model = Author
        fields = ('name', 'bio')


# class RecipeForm(forms.ModelForm):
#     class Meta():
#         model = Recipe
#         fields = ('title', 'author', 'description',
#                   'time_required', 'instructions')


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=400)
    time_required = forms.IntegerField()
    instructions = forms.CharField(widget=forms.Textarea)
