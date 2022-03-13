from rest_framework import serializers
from courses_and_internship.models import (Courses, InternShip)


class CoursesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Courses
        fields = '__all__'


class InternShipSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = InternShip
        fields = '__all__'

    