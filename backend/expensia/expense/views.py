from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny


class ExpenseCategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (AllowAny,)

    def filter_queryset(self, queryset):
        qs = super(ExpenseViewSet, self).filter_queryset(queryset)

        if self.request.method == "GET":
            pass
        return qs

