from rest_framework import viewsets
from courses_and_internship.models import (Courses, InternShip)
from courses_and_internship.serializers import (CoursesSerializers, InternShipSerializers)


class CoursesAPIView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializers
    queryset = Courses.objects.all()


    def perform_create(self, serializer):
        user = self.request.user

        if user.user_type == 'education_centre':
            serializer.save(user=user)
    
        


class InternShipAPIView(viewsets.ModelViewSet):
    serializer_class = InternShipSerializers
    queryset = InternShip.objects.all()


    def perform_create(self, serializer):
        user = self.request.user

        if user.user_type == 'employer':
            serializer.save(user=user)




