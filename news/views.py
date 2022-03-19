from urllib import request
from rest_framework import viewsets
from news.models import News
from news.serializers import (NewsSerializers)
# from news.models import (NewsNonProfitOrganization, NewsTeacherProfile, NewsEmployerProfile, NewsEducationCentre)
# from news.serializers import (NewsNonProfitOrganizationSerializers, NewsEducationCentreSerializers, NewsEmployerProfileSerializers, NewsTeacherProfileSerializers)
from authentications.models import (EducationCentreProfile, TeacherProfile, EmployerProfile, NonProfitOrganizationProfile)




# class NewsNonProfitOrganizationAPIView(viewsets.ModelViewSet):
#     serializer_class = NewsNonProfitOrganizationSerializers
#     queryset = NewsNonProfitOrganization.objects.all()

#     def perform_create(self, serializer):
#         nonprofitorganization1 = NonProfitOrganizationProfile.objects.filter(user=self.request.user).first()
#         user = self.request.user
        
#         if user.user_type == 'non_profit_organization':
#             serializer.save(user=user, nonprofitorganization=nonprofitorganization1)


# class NewsTeacherProfileAPIView(viewsets.ModelViewSet):
#     serializer_class = NewsTeacherProfileSerializers
#     queryset = NewsTeacherProfile.objects.all()

#     def perform_create(self, serializer):
#         teacher1 = TeacherProfile.objects.filter(user=self.request.user).first()
#         user = self.request.user
        
#         if user.user_type == 'teacher':
#             serializer.save(user=user, teacher=teacher1)


# class NewsEducationCentreAPIView(viewsets.ModelViewSet):
#     serializer_class = NewsEducationCentreSerializers
#     queryset = NewsEducationCentre.objects.all()

#     def perform_create(self, serializer):
#         educationcentre = EducationCentreProfile.objects.filter(user=self.request.user).first()
#         user = self.request.user
        
#         if user.user_type == 'education_centre':
#             serializer.save(user=user, centre=educationcentre)


# class NewsEmployerProfileAPIView(viewsets.ModelViewSet):
#     serializer_class = NewsEmployerProfileSerializers
#     queryset = NewsEmployerProfile.objects.all()

#     def perform_create(self, serializer):
#         employer1 = EmployerProfile.objects.filter(user=self.request.user).first()
#         user = self.request.user
        
#         if user.user_type == 'employer':
#             serializer.save(user=user, employer=employer1)


class NewsAPIView(viewsets.ModelViewSet):
    serializer_class = NewsSerializers
    queryset = News.objects.all()

    def perform_create(self, serializer):
        nonprofitorganization1 = NonProfitOrganizationProfile.objects.filter(user=self.request.user).first()
        teacher1 = TeacherProfile.objects.filter(user=self.request.user).first()
        educationcentre = EducationCentreProfile.objects.filter(user=self.request.user).first()
        employer1 = EmployerProfile.objects.filter(user=self.request.user).first()
        user = self.request.user
        
        if user.user_type == 'non_profit_organization':
            serializer.save(user=user, nonprofitorganization=nonprofitorganization1)

        elif user.user_type == 'teacher':
            serializer.save(user=user, teacher=teacher1)

        elif user.user_type == 'education_centre':
            serializer.save(user=user, centre=educationcentre)

        elif user.user_type == 'employer':
            serializer.save(user=user, employer=employer1)