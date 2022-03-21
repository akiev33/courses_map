from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate, password_validation
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import UserProfile, EducationCentreProfile, TeacherProfile, NonProfitOrganizationProfile, EmployerProfile

User = get_user_model()


USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('education_centre', 'EducationCentre'),
        ('teacher', 'Teacher'),
        ('non_profit_organization', 'Non-profit Organization'),
        ('employer', 'Employer')
    )


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, required=True, write_only=True)
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = [
            'user_type',
            'image', 'first_name', 'last_name', 'father_name', 'email', 'phone_number',
            'password', 'password_confirmation',
        ]

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists:
            raise serializers.ValidationError('user with given email  exist')
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError("doesn't much")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        if user.user_type == 'user':
            profile = UserProfile.objects.create(user=user,
                                                 first_name=user.first_name,
                                                 last_name=user.last_name,
                                                 father_name=user.father_name,
                                                 phone_number=user.phone_number,
                                                 email=user.email)
            profile.save()

        elif user.user_type == 'education_centre':
            profile = EducationCentreProfile.objects.create(user=user, first_name=user.first_name,
                                                            last_name=user.last_name,
                                                            father_name=user.father_name,
                                                            phone_number=user.phone_number,
                                                            email=user.email)
            profile.save()

        elif user.user_type == 'teacher':
            profile = TeacherProfile.objects.create(user=user, first_name=user.first_name,
                                                    last_name=user.last_name,
                                                    father_name=user.father_name,
                                                    phone_number=user.phone_number,
                                                    email=user.email)
            profile.save()

        elif user.user_type == 'non_profit_organization':
            profile = NonProfitOrganizationProfile.objects.create(user=user,
                                                                  first_name=user.first_name,
                                                                  last_name=user.last_name,
                                                                  father_name=user.father_name,
                                                                  phone_number=user.phone_number,
                                                                  email=user.email)
            profile.save()

        elif user.user_type == 'employer':
            profile = EmployerProfile.objects.create(user=user,
                                                     first_name=user.first_name,
                                                     last_name=user.last_name,
                                                     father_name=user.father_name,
                                                     phone_number=user.phone_number,
                                                     email=user.email)
            profile.save()

        return user


class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = [
            'id', 'image', 'first_name', 'last_name', 'father_name', 'email', 'phone_number',
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = UserProfile
        fields = [
            'id', 'image', 'first_name', 'last_name', 'father_name', 'about_self',
            'email', 'phone_number',
        ]

    def update(self, instance, validated_data):
        user = instance.user

        instance.image = validated_data.get('image', instance.image)
        instance.about_self = validated_data.get('about_self', instance.about_self)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        user.email = validated_data.get('email', instance.email)
        user.phone_number = validated_data.get('phone_number', instance.phone_number)
        user.save()

        return instance


class AdminUserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = UserProfile
        fields = [
            'id', 'image', 'first_name', 'last_name', 'father_name', 'about_self',
            'email', 'phone_number',
        ]

    def update(self, instance, validated_data):
        user = instance.user

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        user.first_name = validated_data.get('first_name', instance.first_name)
        user.last_name = validated_data.get('last_name', instance.last_name)
        user.father_name = validated_data.get('father_name', instance.father_name)
        user.email = validated_data.get('email', instance.email)
        user.phone_number = validated_data.get('phone_number', instance.phone_number)
        user.save()

        return instance


class EducationCentreProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = EducationCentreProfile
        fields = [
            'id', 'logo', 'first_name', 'last_name', 'father_name', 'organization_name', 'description', 'instagram',
            'video', 'address', 'number_of_students',
            'email', 'phone_number', 'verification', 'rate',
        ]

    def update(self, instance, validated_data):
        user = instance.user

        instance.logo = validated_data.get('logo', instance.logo)
        instance.description = validated_data.get('description', instance.description)
        instance.instagram = validated_data.get('instagram', instance.instagram)
        instance.video = validated_data.get('video', instance.video)
        instance.address = validated_data.get('address', instance.address)
        instance.number_of_students = validated_data.get('number_of_students', instance.number_of_students)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        user.email = validated_data.get('email', instance.email)
        user.phone_number = validated_data.get('phone_number', instance.phone_number)
        user.save()

        return instance


class AdminEducationCentreProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = EducationCentreProfile
        fields = [
            'id', 'logo', 'first_name', 'last_name', 'father_name', 'organization_name', 'description', 'instagram',
            'video', 'address', 'number_of_students',
            'email', 'phone_number', 'verification', 'rate',
        ]

    def update(self, instance, validated_data):
        user = instance.user

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.verification = validated_data.get('verification', instance.verification)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        user.first_name = validated_data.get('first_name', instance.first_name)
        user.last_name = validated_data.get('last_name', instance.last_name)
        user.father_name = validated_data.get('father_name', instance.father_name)
        user.email = validated_data.get('email', instance.email)
        user.phone_number = validated_data.get('phone_number', instance.phone_number)
        user.save()

        return instance


class TeacherProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = TeacherProfile
        fields = [
            'id', 'avatar', 'first_name', 'last_name', 'father_name', 'description', 'instagram', 'video',
            'address', 'number_of_students', 'work_experience', 'category', 'cost_per_hour', 'time_table',
            'lesson_duration', 'education', 'sale',
            'email', 'phone_number', 'verification', 'rate',
        ]

    def update(self, instance, validated_data):
        user = instance.user

        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.description = validated_data.get('description', instance.description)
        instance.instagram = validated_data.get('instagram', instance.instagram)
        instance.video = validated_data.get('video', instance.video)
        instance.address = validated_data.get('address', instance.address)
        instance.number_of_students = validated_data.get('number_of_students', instance.number_of_students)
        instance.work_experience = validated_data.get('work_experience', instance.work_experience)
        instance.category = validated_data.get('category', instance.category)
        instance.cost_per_hour = validated_data.get('cost_per_hour', instance.cost_per_hour)
        instance.time_table = validated_data.get('time_table', instance.time_table)
        instance.lesson_duration = validated_data.get('lesson_duration', instance.lesson_duration)
        instance.education = validated_data.get('education', instance.education)
        instance.sale = validated_data.get('sale', instance.sale)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        user.email = validated_data.get('email', instance.email)
        user.phone_number = validated_data.get('phone_number', instance.phone_number)
        user.save()

        return instance


class AdminTeacherProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = TeacherProfile
        fields = [
            'id', 'avatar', 'first_name', 'last_name', 'father_name', 'description', 'instagram', 'video',
            'address', 'number_of_students', 'work_experience', 'category', 'cost_per_hour', 'time_table',
            'lesson_duration', 'education', 'sale',
            'email', 'phone_number', 'verification', 'rate',
        ]

    def update(self, instance, validated_data):
        user = instance.user

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.verification = validated_data.get('verification', instance.verification)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        user.first_name = validated_data.get('first_name', instance.first_name)
        user.last_name = validated_data.get('last_name', instance.last_name)
        user.father_name = validated_data.get('father_name', instance.father_name)
        user.email = validated_data.get('email', instance.email)
        user.phone_number = validated_data.get('phone_number', instance.phone_number)
        user.save()

        return instance


class NonProfitOrganizationProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = NonProfitOrganizationProfile
        fields = [
            'id', 'first_name', 'last_name', 'father_name', 'organization_name', 'description',
            'email', 'phone_number',
        ]

    def update(self, instance, validated_data):
        user = instance.user

        instance.organization_name = validated_data.get('organization_name', instance.organization_name)
        instance.description = validated_data.get('description', instance.description)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        user.email = validated_data.get('email', instance.email)
        user.phone_number = validated_data.get('phone_number', instance.phone_number)
        user.save()

        return instance


class AdminNonProfitOrganizationProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = NonProfitOrganizationProfile
        fields = [
            'id', 'first_name', 'last_name', 'father_name', 'organization_name', 'description',
            'email', 'phone_number',
        ]

    def update(self, instance, validated_data):
        user = instance.user

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        user.first_name = validated_data.get('first_name', instance.first_name)
        user.last_name = validated_data.get('last_name', instance.last_name)
        user.father_name = validated_data.get('father_name', instance.father_name)
        user.email = validated_data.get('email', instance.email)
        user.phone_number = validated_data.get('phone_number', instance.phone_number)
        user.save()

        return instance


class EmployerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = EmployerProfile
        fields = [
            'id', 'first_name', 'last_name', 'father_name', 'organization_name', 'description',
            'email', 'phone_number',
        ]

    def update(self, instance, validated_data):
        user = instance.user

        instance.organization_name = validated_data.get('organization_name', instance.organization_name)
        instance.description = validated_data.get('description', instance.description)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        user.email = validated_data.get('email', instance.email)
        user.phone_number = validated_data.get('phone_number', instance.phone_number)
        user.save()

        return instance


class AdminEmployerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = EmployerProfile
        fields = [
            'id', 'first_name', 'last_name', 'father_name', 'organization_name', 'description',
            'email', 'phone_number',
        ]

    def update(self, instance, validated_data):
        user = instance.user

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        instance.save()

        user.first_name = validated_data.get('first_name', instance.first_name)
        user.last_name = validated_data.get('last_name', instance.last_name)
        user.father_name = validated_data.get('father_name', instance.father_name)
        user.email = validated_data.get('email', instance.email)
        user.phone_number = validated_data.get('phone_number', instance.phone_number)
        user.save()

        return instance


class LoginSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('user email not found')
        return value

    def validate(self, attrs):
        email = attrs.get('email')

        password = attrs.pop('password', None)

        if not User.objects.filter(email=email,).exists():
            raise serializers.ValidationError("not found")
        user = authenticate(username=email, password=password)
        if user and user.is_active:
            refresh = self.get_token(user)

            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)

        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True, min_length=6)
    new_password1 = serializers.CharField(required=True, write_only=True, min_length=6)
    new_password2 = serializers.CharField(required=True, write_only=True, min_length=6)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Your old password was entered incorrectly. Please enter it again.')
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': "The two password fields didn't match."})
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user