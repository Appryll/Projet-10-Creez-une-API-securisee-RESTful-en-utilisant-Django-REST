from rest_framework.permissions import BasePermission

class IsAuthorAuthenticated(BasePermission):
    def has_permission(self, request, views):
        return bool(request.user
                    and request.user.is_authenticated
                    and request.user.is_author)
