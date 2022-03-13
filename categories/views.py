from rest_framework import viewsets
from categories.models import (Category)
from categories.serializers import (CategorySerializers)
from categories.permissions import IsAdminOrReadOnly


class CategoryAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
