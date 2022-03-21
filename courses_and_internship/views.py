from rest_framework import viewsets
from courses_and_internship.models import (Courses, InternShip)
from courses_and_internship.serializers import (CoursesSerializers, InternShipSerializers)

from .permissions import IsEducationCentreAndIsOwnerOrReadOnly, IsEmployerCentreAndIsOwnerOrReadOnly


class CoursesAPIView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializers
    permission_classes = [IsEducationCentreAndIsOwnerOrReadOnly]
    queryset = Courses.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
    

class InternShipAPIView(viewsets.ModelViewSet):
    serializer_class = InternShipSerializers
    permission_classes = [IsEmployerCentreAndIsOwnerOrReadOnly]
    queryset = InternShip.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)




