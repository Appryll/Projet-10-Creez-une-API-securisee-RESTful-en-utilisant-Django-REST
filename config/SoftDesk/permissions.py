from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from SoftDesk.models import Projects

class IsAuthorAuthenticated(BasePermission):
    def has_permission(self, request, views):
        return bool(request.user
                    and request.user.is_authenticated
                    and request.user.is_author)

class ViewContributor_ProjectPermissions_(BasePermission):
    def has_permission(self, request, view):
        try:
            project = get_object_or_404(Projects, id=view.kwargs['project_id'])
            if request.method in permissions.SAFE_METHODS:
                return project in Projects.objects.filter(contributor__user=request.user)
            return request.user == project.author_user_id
        except KeyError:
            return True
