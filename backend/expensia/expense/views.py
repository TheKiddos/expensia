from django.shortcuts import render
from .models import Category
from rest_framework.decorartors import api_view
from rest_framework.response import response
from .serializers import CategorySerializer
from django.views import View
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, generics, status, filters
from rest_framework.permissions import IsAuthenticated
"""
@api_view(['POST'])
class CategoryView(ModelViewSet):

    @api_view(['POST'])
    def create_category(request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return response(serializer.data)

    @api_view(['DELETE'])
    def delete_category(equest,id):
        category = Category.objects.get(id=id)
        category.delete()
        return response('category deleted<3')
"""
class ExpenseCategoryView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    permission_classes = (IsAuthenticated,)
