from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to edit or delete objects.
    Read-only access is allowed for everyone (authenticated users).
    """
    def has_permission(self, request, view):
        # Allow read-only methods (GET, HEAD, OPTIONS) for any authenticated request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Otherwise, check if user is an admin
        return request.user and request.user.is_superuser
