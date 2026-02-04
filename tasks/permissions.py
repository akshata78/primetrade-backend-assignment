from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Admin can access everything
        if request.user.role == "ADMIN":
            return True

        # Normal user can access only their own tasks
        return obj.user == request.user
