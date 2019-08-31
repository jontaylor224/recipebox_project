from django import forms
from .models import Recipe, Author
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', )


class AuthorForm(forms.ModelForm):
    class Meta():
        model = Author
        fields = ('bio', )


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=400)
    time_required = forms.IntegerField()
    instructions = forms.CharField(widget=forms.Textarea)
