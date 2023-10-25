from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied
from .models import Wallet


# Custom permission to allow read-only access or ownership-based access
class IsOwnerOrReadOnly(BasePermission):
    message = "You do not have permission to access this object."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # Allow safe methods (e.g., GET, HEAD, OPTIONS)
            return True

        if obj.user == request.user:
            # Allow access if the user is the owner of the object
            return True

        # Deny access and raise a permission denied exception
        raise PermissionDenied(self.message)

# Custom permission for Wallet model to allow read-only access or ownership-based access
class IsOwnerOrReadOnlyWallet(BasePermission):
    message = "You do not have permission to access this object."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # Allow safe methods (e.g., GET, HEAD, OPTIONS)
            return True

        if obj.owner == request.user:
            # Allow access if the user is the owner of the wallet
            return True

        # Deny access and raise a permission denied exception
        raise PermissionDenied(self.message)
