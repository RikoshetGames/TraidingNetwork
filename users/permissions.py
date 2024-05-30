from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    message = "Вы не являетесь модератором или администратором."

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderator').exists() or request.user.is_superuser


class IsSuperUser(BasePermission):
    message = "Вы не являетесь администратором"

    def has_permission(self, request, view):
        return request.user.is_superuser


class IsCreator(BasePermission):
    message = "Вы не владелец данного объекта"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.create_user:
            return request.method in ('GET', 'PUT', 'PATCH', 'DELETE')
        return False


class IsUser(BasePermission):
    """Права доступа для пользователя"""
    message = "Вы не являетесь владельцем этой учетной записи"

    def has_object_permission(self, request, view, obj):
        return request.user == obj
