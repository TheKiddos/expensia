from .models import Category
from .serializers import CategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny


class ExpenseCategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
