from rest_framework import viewsets
from photo.models import (EducationCentrePhoto, TeacherProfilePhoto, EmployerProfilePhoto, NonProfitOrganizationProfilePhoto)
from photo.serializers import (EducationCentrePhotoSerializers, TeacherProfilePhotoSerializers, EmployerProfilePhotoSerializers, NonProfitOrganizationProfilePhotoSerializers)


class EducationCentrePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = EducationCentrePhotoSerializers
    queryset = EducationCentrePhoto.objects.all()


class TeacherProfilePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = TeacherProfilePhotoSerializers
    queryset = TeacherProfilePhoto.objects.all()


class EmployerProfilePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = EmployerProfilePhotoSerializers
    queryset = EmployerProfilePhoto.objects.all()


class NonProfitOrganizationProfilePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = NonProfitOrganizationProfilePhotoSerializers
    queryset = NonProfitOrganizationProfilePhoto.objects.all()