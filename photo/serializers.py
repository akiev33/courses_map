from rest_framework import serializers
from photo.models import (EducationCentrePhoto, TeacherProfilePhoto, NonProfitOrganizationProfilePhoto, EmployerProfilePhoto)


class EducationCentrePhotoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = EducationCentrePhoto
        fields = '__all__'


class TeacherProfilePhotoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = TeacherProfilePhoto
        fields = '__all__'


class NonProfitOrganizationProfilePhotoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = NonProfitOrganizationProfilePhoto
        fields = '__all__'


class EmployerProfilePhotoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = EmployerProfilePhoto
        fields = '__all__'