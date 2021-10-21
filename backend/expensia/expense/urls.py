from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import (
    ExpenseViewSet, ExpenseCategoryView,
)

router = DefaultRouter()

router.register("expense-category", ExpenseCategoryView.as_view, basename="expense_category")

urlpatterns = router.urls

urlpatterns +=  (
    path("expense-category/<int:pk>", ExpenseCategoryView.as_view(), name='expense_category'),
)