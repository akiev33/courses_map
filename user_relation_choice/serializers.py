from rest_framework import serializers
from user_relation_choice.models import (UserRelationChoiceEducationCentreProfile, UserRelationChoiceTeacherProfile, UserRelationChoiceCourses, UserRelationChoiceInternShip)

from authentications.models import EducationCentreProfile, TeacherProfile
from courses_and_internship.models import Courses, InternShip


class UserRelationChoiceEducationCentreProfileSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = UserRelationChoiceEducationCentreProfile
        fields = [
            'id', 'user', 'profile', 'rate', 'comments'
        ]

    def create(self, validated_data):
        relation_choice = UserRelationChoiceEducationCentreProfile.objects.create(**validated_data)

        profile = EducationCentreProfile.objects.filter(id=relation_choice.profile.id).first()
        profile.number_of_comments += 1
        profile.sum_of_rate += relation_choice.rate
        profile.rate = round((profile.sum_of_rate / profile.number_of_comments), 1)
        profile.save()

        return relation_choice


class UserRelationChoiceTeacherProfileSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = UserRelationChoiceTeacherProfile
        fields = [
            'id', 'user', 'profile', 'rate', 'comments'
        ]

    def create(self, validated_data):
        relation_choice = UserRelationChoiceTeacherProfile.objects.create(**validated_data)

        profile = TeacherProfile.objects.filter(id=relation_choice.profile.id).first()
        profile.number_of_comments += 1
        profile.sum_of_rate += relation_choice.rate
        profile.rate = round((profile.sum_of_rate / profile.number_of_comments), 1)
        profile.save()

        return relation_choice


class UserRelationChoiceCoursesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = UserRelationChoiceCourses
        fields = [
            'id', 'user', 'course', 'rate', 'comments'
        ]

    def create(self, validated_data):
        relation_choice = UserRelationChoiceCourses.objects.create(**validated_data)

        course = Courses.objects.filter(id=relation_choice.course.id).first()
        course.number_of_comments += 1
        course.sum_of_rate += relation_choice.rate
        course.rate = round((course.sum_of_rate / course.number_of_comments), 1)
        course.save()

        return relation_choice


class UserRelationChoiceInternShipSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = UserRelationChoiceInternShip
        fields = [
            'id', 'user', 'internship', 'rate', 'comments'
        ]

    def create(self, validated_data):
        relation_choice = UserRelationChoiceInternShip.objects.create(**validated_data)

        internship = InternShip.objects.filter(id=relation_choice.internship.id).first()
        internship.number_of_comments += 1
        internship.sum_of_rate += relation_choice.rate
        internship.rate = round((internship.sum_of_rate / internship.number_of_comments), 1)
        internship.save()

        return relation_choice
