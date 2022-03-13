from django.shortcuts import render
from django.contrib.auth import get_user_model, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from rest_framework_simplejwt.views import TokenObtainPairView

from authentications.serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer,\
                                        UserProfileSerializer, EducationCentreProfileSerializer,\
                                        TeacherProfileSerializer, NonProfitOrganizationProfileSerializer,\
                                        EmployerProfileSerializer

from rest_framework.generics import UpdateAPIView, CreateAPIView, RetrieveUpdateAPIView
from authentications.email import email_send

from .permissions import IsOwnerOrStaffOrReadOnly
from .models import UserProfile, EducationCentreProfile, TeacherProfile, NonProfitOrganizationProfile, EmployerProfile

User = get_user_model()


class UserRegisterApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            if user:
                email_send(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActivationView(View):

    def get(self, request, activation_code):

        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return render(request, 'index.html', {})

        except User.DoesNotExist:
            return render(request, 'link_exp.html', {})


class LoginApiView(TokenObtainPairView):
    serializer_class = LoginSerializer


class LogoutApiView(APIView):
    model = User

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UserProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    lookup_field = "id"

    def list(self, request):
        user = request.user
        query = UserProfile.objects.all(user=user)
        serializer = UserProfileSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        user = self.request.user

        if user.is_staff:
            serializer.save(first_name=self.request.data.get('first_name'),
                            last_name=self.request.data.get('last_name'),
                            father_name=self.request.data.get('father_name'),
                            )


class EducationCentreProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = EducationCentreProfileSerializer
    queryset = EducationCentreProfile.objects.all()
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    lookup_field = "id"

    def list(self, request):
        user = request.user
        query = EducationCentreProfile.objects.all(user=user)
        serializer = EducationCentreProfileSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        user = self.request.user

        if user.is_staff:
            serializer.save(first_name=self.request.data.get('first_name'),
                            last_name=self.request.data.get('last_name'),
                            father_name=self.request.data.get('father_name'),
                            verification=self.request.data.get('verification')
                            )


class TeacherProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = TeacherProfileSerializer
    queryset = TeacherProfile.objects.all()
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    lookup_field = "id"

    def list(self, request):
        user = request.user
        query = TeacherProfile.objects.all(user=user)
        serializer = TeacherProfileSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        user = self.request.user

        if user.is_staff:
            serializer.save(first_name=self.request.data.get('first_name'),
                            last_name=self.request.data.get('last_name'),
                            father_name=self.request.data.get('father_name'),
                            verification=self.request.data.get('verification')
                            )


class NonProfitOrganizationProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = NonProfitOrganizationProfileSerializer
    queryset = NonProfitOrganizationProfile.objects.all()
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    lookup_field = "id"

    def list(self, request):
        user = request.user
        query = NonProfitOrganizationProfile.objects.all(user=user)
        serializer = NonProfitOrganizationProfileSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        user = self.request.user

        if user.is_staff:
            serializer.save(first_name=self.request.data.get('first_name'),
                            last_name=self.request.data.get('last_name'),
                            father_name=self.request.data.get('father_name'),
                            )


class EmployerProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = EmployerProfileSerializer
    queryset = EmployerProfile.objects.all()
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    lookup_field = "id"

    def list(self, request):
        user = request.user
        query = EmployerProfile.objects.all(user=user)
        serializer = EmployerProfileSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        user = self.request.user

        if user.is_staff:
            serializer.save(first_name=self.request.data.get('first_name'),
                            last_name=self.request.data.get('last_name'),
                            father_name=self.request.data.get('father_name'),
                            )
