from rest_framework.viewsets import ModelViewSet

from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer
from .filters import ExpenseFilter


class ExpenseCategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filterset_class = ExpenseFilter
