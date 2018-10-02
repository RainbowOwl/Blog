from rest_framework import permissions

from apps.custom_auth.enums import RoleTypes


class BasePermissions(permissions.BasePermission):
    message = 'Access denied'


class RoleIsAdministrator(BasePermissions):

    def has_permission(self, request, view):
        if not hasattr(request.user, 'role'):
            return False
        return request.user.role in (RoleTypes.ADMINISTRATOR,)


class RoleIsAdministratorOrManager(BasePermissions):

    def has_permission(self, request, view):
        if not hasattr(request.user, 'role'):
            return False
        return request.user.role in (RoleTypes.ADMINISTRATOR,
                                     RoleTypes.MANAGER)