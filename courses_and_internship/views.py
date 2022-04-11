from rest_framework import viewsets
from courses_and_internship.models import (Courses, InternShip)
from courses_and_internship.serializers import (CoursesSerializers, InternShipSerializers)

from .permissions import IsEducationCentreAndIsOwnerOrReadOnly, IsEmployerCentreAndIsOwnerOrReadOnly
from authentications.models import EducationCentreProfile, EmployerProfile

from django_filters.rest_framework import DjangoFilterBackend


class CoursesAPIView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializers
    permission_classes = [IsEducationCentreAndIsOwnerOrReadOnly]
    queryset = Courses.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category']

    def perform_create(self, serializer):
        user = self.request.user
        user_profile = EducationCentreProfile.objects.filter(user=user).first()
        serializer.save(user=user, organization=user_profile)
        


class InternShipAPIView(viewsets.ModelViewSet):
    serializer_class = InternShipSerializers
    permission_classes = [IsEmployerCentreAndIsOwnerOrReadOnly]
    queryset = InternShip.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        user_profile = EmployerProfile.objects.filter(user=user).first()
        serializer.save(user=user, employer=user_profile)
