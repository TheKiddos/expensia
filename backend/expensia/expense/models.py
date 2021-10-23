from django.db import models
from rest_framework.reverse import reverse


class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    icon = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('expense:category-detail', args=(self.pk,))
