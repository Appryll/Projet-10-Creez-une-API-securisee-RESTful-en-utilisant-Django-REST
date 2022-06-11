from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from SoftDesk.models import Projects, Comments

class IsAuthorAuthenticated(BasePermission):
    def has_permission(self, request, views):
        return bool(request.user
                    and request.user.is_authenticated
                    and request.user.is_author)

class PermissionsViewContributor(BasePermission):
    def has_permission(self, request, view):
        try:
            project = get_object_or_404(Projects, id=view.kwargs['project_id'])
            if request.method in permissions.SAFE_METHODS:
                return project in Projects.objects.filter(contributor__user=request.user)
            return request.user == project.author_user_id
        except KeyError:
            return True

class PermissionsCommentAuthor(BasePermission):
    message = "You do not have permission to perform this action."
    def has_permission(self, request, view):
        comment = get_object_or_404(Comments, id=view.kwargs['comment_id'])
        # print(comment.author_user_id.id)
        # print(request.user.id)
        if request.user.id == comment.author_user_id.id:
            return True
        return False
        
        
