from rest_framework import permissions
from marketplace.apps.authentication.models import Customer


class IsCustomer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return Customer.objects.filter(user=request.user).exists()


class IsOwnerOrStaff(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        # Write permissions are only allowed to the owner of the object.
        return (obj.user == request.user or request.user.is_staff)
