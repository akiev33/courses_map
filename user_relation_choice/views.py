from rest_framework import viewsets
from user_relation_choice.models import (UserRelationChoiceTeacherProfile, UserRelationChoiceEducationCentreProfile, UserRelationChoiceInternShip, UserRelationChoiceCourses)
from user_relation_choice.serializers import (UserRelationChoiceEducationCentreProfileSerializers, UserRelationChoiceTeacherProfileSerializers, UserRelationChoiceInternShipSerializers, UserRelationChoiceCoursesSerializers)


class UserRelationChoiceTeacherProfileAPIView(viewsets.ModelViewSet):
    serializer_class = UserRelationChoiceTeacherProfileSerializers
    queryset = UserRelationChoiceTeacherProfile.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class UserRelationChoiceEducationCentreProfileAPIView(viewsets.ModelViewSet):
    serializer_class = UserRelationChoiceEducationCentreProfileSerializers
    queryset = UserRelationChoiceEducationCentreProfile.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class UserRelationChoiceInternShipAPIView(viewsets.ModelViewSet):
    serializer_class = UserRelationChoiceInternShipSerializers
    queryset = UserRelationChoiceInternShip.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class UserRelationChoiceCoursesAPIView(viewsets.ModelViewSet):
    serializer_class = UserRelationChoiceCoursesSerializers
    queryset = UserRelationChoiceCourses.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()