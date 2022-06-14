from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from SoftDesk.models import Projects, Comments, Issues


class PermissionsViewContributor(BasePermission):
    def has_permission(self, request, view):
        try:
            project = get_object_or_404(Projects, id=view.kwargs['project_id'])
            if request.method in permissions.SAFE_METHODS:
                return project in Projects.objects.filter(contributor__user=request.user)
            return request.user == project.author_user_id
        except KeyError:
            return True

class PermissionsProjectAuthor(BasePermission):
    message = "You do not have permission to perform this action. Must have copyright permission."
    def has_permission(self, request, view):
        project = get_object_or_404(Projects, id=view.kwargs['project_id'])
        if request.user.id == project.author_user_id.id:
            return True
        return False

class PermissionsContributorAuthorProjet(BasePermission):
    message = "You do not have permission to perform this action. Must have copyright permissionYou \
    are a contributor and cannot modify or delete other contributors. You must have author permissions."
    def has_permission(self, request, view):
        project = get_object_or_404(Projects, id=view.kwargs['project_id'])
        if request.user.id == project.author_user_id.id:
            return True
        return False

class PermissionsIssueAuthor(BasePermission):
    message = "You do not have permission to perform this action."
    def has_permission(self, request, view):
        issue = get_object_or_404(Issues, id=view.kwargs['issue_id'])
        if request.user.id == issue.author_user_id.id:
            return True
        return False

class PermissionsCommentAuthor(BasePermission):
    message = "You do not have permission to perform this action."
    def has_permission(self, request, view):
        comment = get_object_or_404(Comments, id=view.kwargs['comment_id'])
        if request.user.id == comment.author_user_id.id:
            return True
        return False
