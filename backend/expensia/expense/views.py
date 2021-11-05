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
    filter_fields = ("start_date", "end_date")
    lookup_field = "id"

    def get_serializer_context(self):
        ctx = super(ExpenseViewSet, self).get_serializer_context()
        ctx["request"] = self.request
        return ctx