from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(BasePermission):
    message = "You do not have permission to access this object."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if obj.user == request.user:
            return True

        raise PermissionDenied(self.message)

class IsWalletAndUserPositionOwner(BaseException):
    message = "You do not have permission to access this object."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if obj.owner == request.user:
            return True

        raise PermissionDenied(self.message)