from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied


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
