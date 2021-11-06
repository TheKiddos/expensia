from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel
from rest_framework.reverse import reverse


class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    icon = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('expense:category-detail', args=(self.pk,))


class Expense(TimeStampedModel):
    """ Expense model """

    name =models.CharField(_("Name"), max_length=30, blank=False, null=False)
    amount = models.DecimalField(
        _("Amount"), max_digits=20, decimal_places=3, blank=False, null=False
    )
    category = models.ForeignKey(Category,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("expense:expense_details", args=(self.id,))

    def get_amount(self):
        return Decimal(self.amount)


