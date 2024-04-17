import django_filters
from django import forms
from .models import Recipe, Category
from django.db.models import F

from django.forms import ModelForm


class RecipeFilter(django_filters.FilterSet):
    categories = django_filters.ModelMultipleChoiceFilter(
        field_name='categories',
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Recipe
        fields = ['categories']
