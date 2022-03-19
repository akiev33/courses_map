from rest_framework import generics

from rest_framework import status
from rest_framework.response import Response

from .models import Favorite
from .serializers import FavoriteCreateSerializers


class FavoriteCreateAPIView(generics.CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializers
    
    def get_serializer_context(self):
        return {
            "user": self.request.user
        }


class FavoriteAPIView(generics.ListAPIView):
    serializer_class = FavoriteCreateSerializers

    def get_queryset(self):
        queryset = Favorite.objects.filter(user_id=self.request.user)
        return queryset


class FavoriteDeleteAPIView(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializers
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Favorite.objects.filter(user_id=self.request.user)
        return queryset