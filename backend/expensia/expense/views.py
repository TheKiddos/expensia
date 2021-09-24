from django.shortcuts import render

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, generics, status, filters

from .models import Expense, ExpenseCategory
from .serializer import ExpenseSerializer, ExpenseCategorySerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated,)
    filter_fields = ("start_date", "end_date")
    lookup_field = "id"

    def get_serializer_context(self):
        ctx = super(ExpenseViewSet, self).get_serializer_context()
        ctx["request"] = self.request
        return ctx


class ExpenseCategoryView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    permission_classes = (IsAuthenticated,)

