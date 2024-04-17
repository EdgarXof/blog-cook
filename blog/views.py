from django.shortcuts import render, HttpResponse

from blog.models import Recipe
from django.http import Http404


def index(request):
    items = Recipe.objects.all()
    return render(request, "recipes.html", {"recipes": items})


def detail(request, recipe_id):
    # FIXME
    #  If I load the page with a non existing ID, I get an error "Http500", I should get a "Http404".
    #  - Test if the recipe exists
    #    - if yes, retrieve it
    #    - if no, raise an Http404 error
    try:
        recipe_object = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    return render(request, "recipes-detail.html", {"recipe": recipe_object})
