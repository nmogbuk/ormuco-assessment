from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30, unique=True)
    favorite_color = models.CharField(max_length=20)
    cats_or_dogs = models.CharField(max_length=20)