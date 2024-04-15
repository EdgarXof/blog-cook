from django.shortcuts import render, HttpResponse

from blog.models import Recipe


def index(request):
    items = Recipe.objects.all()
    return render(request, "recipes.html", {"recipes": items})


def detail(request, recipe_id):
    recipe_object = Recipe.objects.get(pk=recipe_id)
    return render(request, "recipes-detail.html", {"recipe": recipe_object})
