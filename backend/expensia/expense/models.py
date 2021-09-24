from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from decimal import Decimal

# Create your models here.


class ExpenseCategory(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text='Keep the name short, if you can make it just one word.',
    )
    icon = models.ImageField(upload_to="images", help_text='Upload the category icon',)


class Expense(models.Model):
    """ Expense model """

    name =models.CharField(_("Name"), max_length=30, blank=False, null=False)
    start_date = models.DateTimeField(_("Start Date"), null=False, blank=False)
    end_date = models.DateTimeField(_("End Date"), null=False, blank=False)
    amount = models.DecimalField(
        _("Amount"), max_digits=20, decimal_places=3, blank=False, null=False
    )
    category = models.ManyToManyField(ExpenseCategory, blank=False, related_name='categories')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("expense:expense_details", args=(self.id,))

    def get_amountt(self):
        return Decimal(self.amount)

    def get_categories(self):
        category_str = ""
        for ct in self.category.active():
            category_str += f"{ct.name}, "
        return category_str[:-2] if category_str else ""