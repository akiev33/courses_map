from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsEducationCentreAndIsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_authenticated and
            (request.user.is_staff or
             (obj.user == request.user and
              request.user.user_type == "education_centre"))
             )

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or \
               request.user and (request.user.user_type == "education_centre" or request.user.is_staff)


class IsEmployerCentreAndIsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_authenticated and
            (request.user.is_staff or
             (obj.user == request.user and
              request.user.user_type == "employer"))
        )

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or \
               request.user and (request.user.user_type == "employer" or request.user.is_staff)
