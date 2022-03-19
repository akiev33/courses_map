from rest_framework import serializers
# from news.models import (NewsNonProfitOrganization, NewsEducationCentre, NewsEmployerProfile, NewsTeacherProfile)
from news.models import (News)


class NewsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = '__all__'





# class NewsNonProfitOrganizationSerializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = NewsNonProfitOrganization
#         fields = '__all__'


# class NewsEducationCentreSerializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = NewsEducationCentre
#         fields = '__all__'


# class NewsEmployerProfileSerializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = NewsEmployerProfile
#         fields = '__all__'


# class NewsTeacherProfileSerializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = NewsTeacherProfile
#         fields = '__all__'