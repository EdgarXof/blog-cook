import django_filters
from django import forms
from .models import Recipe, Category
from django.forms import ModelForm


class RecipeForm(ModelForm):
    recipe = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Recipe
        fields = ['category']
