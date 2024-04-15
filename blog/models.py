from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200)


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
