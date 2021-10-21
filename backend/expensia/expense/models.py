from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    icon = models.ImageField()

# Create your models here.
