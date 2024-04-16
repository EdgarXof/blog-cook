from django.db import models


# Create your models here.
class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200)


class Recipe(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    # FIXME: You need to run once:
    #  - python ./manage.py makemigrations
    #  - python ./manage.py migrate
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
