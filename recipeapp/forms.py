from django import forms
from .models import Recipe, Author
from django.contrib.auth.models import User


class AuthorForm(forms.Form):
    username = forms.CharField(max_length=200)
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=32)
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=32)
    bio = forms.CharField(widget=forms.Textarea)


class UserRecipeForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=400)
    time_required = forms.IntegerField(label="Time Required (minutes)")
    instructions = forms.CharField(widget=forms.Textarea)


class AdminRecipeForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=400)
    time_required = forms.IntegerField(label="Time Required (minutes)")
    instructions = forms.CharField(widget=forms.Textarea)
