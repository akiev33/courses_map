from rest_framework import serializers
from courses_and_internship.models import (Courses, InternShip)
from django.contrib.auth import get_user_model


User = get_user_model()


class CoursesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Courses
        fields = [
            'id', 'organization', 'whats_app', 'courses_name', 'description', 'phone_number', 'email',
            'instagram', 'video', 'address', 'number_of_free_places', 'category', 'cost_per_month',
            'time_table', 'lesson_duration', 'programm', 'sale', 'formats', 'courses_duration', 'rate',
        ]

    def create(self, validated_data):
        course = Courses.objects.create(user=validated_data.get('user'),
                                        organization=validated_data.get('organization'),
                                        whats_app=validated_data.get('whats_app'),
                                        courses_name=validated_data.get('courses_name'),
                                        description=validated_data.get('description'),
                                        phone_number=validated_data.get('phone_number'),
                                        email=validated_data.get('email'),
                                        instagram=validated_data.get('instagram'), video=validated_data.get('video'),
                                        number_of_free_places=validated_data.get('number_of_free_places'),
                                        cost_per_month=validated_data.get('cost_per_month'),
                                        time_table=validated_data.get('time_table'),
                                        lesson_duration=validated_data.get('lesson_duration'),
                                        programm=validated_data.get('programm'),
                                        sale=validated_data.get('sale'), formats=validated_data.get('formats'),
                                        courses_duration=validated_data.get('courses_duration')
                                        )
        course.category.set(validated_data.get('category'))
        course.save()

        return course

    def update(self, instance, validated_data):
        instance.whats_app = validated_data.get('whats_app', instance.whats_app)
        instance.courses_name = validated_data.get('courses_name', instance.courses_name)
        instance.description = validated_data.get('description', instance.description)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.instagram = validated_data.get('instagram', instance.instagram)
        instance.video = validated_data.get('video', instance.video)
        instance.address = validated_data.get('address', instance.address)
        instance.number_of_free_places = validated_data.get('number_of_free_places', instance.number_of_free_places)
        instance.category.set(validated_data.get('category', instance.category))
        instance.cost_per_month = validated_data.get('cost_per_month', instance.cost_per_month)
        instance.time_table = validated_data.get('time_table', instance.time_table)
        instance.lesson_duration = validated_data.get('lesson_duration', instance.lesson_duration)
        instance.programm = validated_data.get('programm', instance.programm)
        instance.sale = validated_data.get('sale', instance.sale)
        instance.formats = validated_data.get('formats', instance.formats)
        instance.courses_duration = validated_data.get('courses_duration', instance.courses_duration)

        instance.save()

        return instance


class InternShipSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = InternShip
        fields = [
            'id', 'employer', 'description', 'salary', 'time_table', 'duration', 'position', 'rate',
        ]

    def create(self, validated_data):
        internship = InternShip.objects.create(user=validated_data.get('user'),
                                               employer=validated_data.get('employer'),
                                               description=validated_data.description,
                                               salary=validated_data.salary, time_table=validated_data.time_table,
                                               duration=validated_data.duration, position=validated_data.position,
                                               )

        internship.save()

        return internship

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.time_table = validated_data.get('time_table', instance.time_table)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.position = validated_data.get('position', instance.position)

        instance.save()

        return instance
    