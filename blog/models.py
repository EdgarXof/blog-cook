from django.db import models


# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.label

    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200)


class Recipe(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
