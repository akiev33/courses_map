from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from favorite.models import Favorite

from favorite.serializers import FavoriteSerializers
from favorite.permissions import IsOwnerOnly


class FavoriteAPIView(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializers
    permission_classes = [IsOwnerOnly]
    queryset = Favorite.objects.all()

    def list(self, request, *args, **kwargs):
        owner = request.user
        query = Favorite.objects.filter(user=owner)
        serializer = FavoriteSerializers(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        if self.request.user.user_type == 'user':
            serializer.save(user=self.request.user)