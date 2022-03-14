from urllib import request
from rest_framework import viewsets
from photo.models import (EducationCentrePhoto, TeacherProfilePhoto, EmployerProfilePhoto, NonProfitOrganizationProfilePhoto)
from photo.serializers import (EducationCentrePhotoSerializers, TeacherProfilePhotoSerializers, EmployerProfilePhotoSerializers, NonProfitOrganizationProfilePhotoSerializers)
from authentications.models import EducationCentreProfile, TeacherProfile, EmployerProfile, NonProfitOrganizationProfile


class EducationCentrePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = EducationCentrePhotoSerializers
    queryset = EducationCentrePhoto.objects.all()

    def perform_create(self, serializer):
        educationcentre = EducationCentreProfile.objects.filter(user=self.request.user).first()
        user = self.request.user
        
        if user.user_type == 'education_centre':
            serializer.save(user=user, centre=educationcentre)


class TeacherProfilePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = TeacherProfilePhotoSerializers
    queryset = TeacherProfilePhoto.objects.all()

    def perform_create(self, serializer):
        teacher1 = TeacherProfile.objects.filter(user=self.request.user).first()
        user = self.request.user
        
        if user.user_type == 'teacher':
            serializer.save(user=user, teacher=teacher1)


class EmployerProfilePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = EmployerProfilePhotoSerializers
    queryset = EmployerProfilePhoto.objects.all()

    def perform_create(self, serializer):
        employer1 = EmployerProfile.objects.filter(user=self.request.user).first()
        user = self.request.user
        
        if user.user_type == 'employer':
            serializer.save(user=user, employer=employer1)


class NonProfitOrganizationProfilePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = NonProfitOrganizationProfilePhotoSerializers
    queryset = NonProfitOrganizationProfilePhoto.objects.all()

    def perform_create(self, serializer):
        nonprofitorganization1 = NonProfitOrganizationProfile.objects.filter(user=self.request.user).first()
        user = self.request.user
        
        if user.user_type == 'non_profit_organization':
            serializer.save(user=user, nonprofitorganization=nonprofitorganization1)