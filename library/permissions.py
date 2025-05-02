from rest_framework import permissions
from users.models import User

class IsLibrarian(permissions.BasePermission):
    """
    Permission to allow only librarians.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'is_librarian', False)


class IsMember(permissions.BasePermission):
    """
    Permission to allow only members.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and getattr(request.user, 'role', None) == User.MEMBER
