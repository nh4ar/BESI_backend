from rest_framework import permissions


class OwnDeployment(permissions.BasePermission):
    """
    Object level permission to access a information from a deployment
    """

    def has_object_permission(self, request, view, obj):
        return obj.deployment == request.user or request.user.is_staff
