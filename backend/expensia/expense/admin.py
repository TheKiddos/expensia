from django.contrib import admin
from .models import Category, Expense

# Register your models here.



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
        return self.list_display


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category)