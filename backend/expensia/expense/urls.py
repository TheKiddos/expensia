from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    ExpenseCategoryView,
)

app_name = 'expense'

router = DefaultRouter()

router.register('category', ExpenseCategoryView, basename='category')
router.register('expense', ExpenseViewSet, basename='expense')

urlpatterns = router.urls
