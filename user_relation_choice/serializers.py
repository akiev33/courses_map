from rest_framework import serializers
from user_relation_choice.models import (UserRelationChoiceEducationCentreProfile, UserRelationChoiceTeacherProfile, UserRelationChoiceCourses, UserRelationChoiceInternShip)


class UserRelationChoiceEducationCentreProfileSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = UserRelationChoiceEducationCentreProfile
        fields = [
            'id', 'user', 'profile', 'rate', 'comments'
        ]


class UserRelationChoiceTeacherProfileSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = UserRelationChoiceTeacherProfile
        fields = [
            'id', 'user', 'profile', 'rate', 'comments'
        ]


class UserRelationChoiceCoursesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = UserRelationChoiceCourses
        fields = [
            'id', 'user', 'profile', 'rate', 'comments'
        ]


class UserRelationChoiceInternShipSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = UserRelationChoiceInternShip
        fields = [
            'id', 'user', 'profile', 'rate', 'comments'
        ]