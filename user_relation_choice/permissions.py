from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsDefaultUserAndIsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_authenticated and
            (request.user.is_staff or
             (obj.user == request.user and
              request.user.user_type == "user"))
             )

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or \
               request.user and (request.user.user_type == "user" or request.user.is_staff)
