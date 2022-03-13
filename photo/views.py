from rest_framework import viewsets
from photo.models import (EducationCentrePhoto, TeacherProfilePhoto, EmployerProfilePhoto, NonProfitOrganizationProfilePhoto)
from photo.serializers import (EducationCentrePhotoSerializers, TeacherProfilePhotoSerializers, EmployerProfilePhotoSerializers, NonProfitOrganizationProfilePhotoSerializers)



class EducationCentrePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = EducationCentrePhotoSerializers
    queryset = EducationCentrePhoto.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        
        if user.user_type == 'education_centre':
            serializer.save(user=user)




class TeacherProfilePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = TeacherProfilePhotoSerializers
    queryset = TeacherProfilePhoto.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        
        if user.user_type == 'teacher':
            serializer.save(user=user)


class EmployerProfilePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = EmployerProfilePhotoSerializers
    queryset = EmployerProfilePhoto.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        
        if user.user_type == 'employer':
            serializer.save(user=user)


class NonProfitOrganizationProfilePhotoAPIView(viewsets.ModelViewSet):
    serializer_class = NonProfitOrganizationProfilePhotoSerializers
    queryset = NonProfitOrganizationProfilePhoto.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        
        if user.user_type == 'non_profit_organization':
            serializer.save(user=user)