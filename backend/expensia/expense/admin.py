
from __future__ import unicode_literals

from django.contrib import admin


from .models import Expense, ExpenseCategory
# Register your models here.


class ExpenseCategoryAdmin(admin.ModelAdmin):
    model = ExpenseCategory
    list_display = ('name', 'icon')
    list_filter = ('name',)
    search_fields = ('name',)
    order = ['-created']

    def has_add_permission(self, request, obj=None):
        return True


class ExpenseAdmin(admin.ModelAdmin):

    model = Expense
    date_hierarchy = 'start_date'
    list_display = ('name', 'amount', 'start_date', 'end_date',)
    list_filter = ('start_date', 'end_date', 'category')
    filter_horizontal = ('category',)
    order = ['-start_date']
    fieldsets = (
        (None, {'fields': (
            'name', 'amount', 'start_date', 'end_date', 'category',)}),
    )

    def has_add_permission(self, request, obj=None):
        return True

    def get_list_display(self, request):
        """
        Return a sequence containing the fields to be displayed on the
        changelist.
        """
        # if request.GET.get('category__id__exact', None):
        #     return self.custom_list_display
        return self.list_display


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)