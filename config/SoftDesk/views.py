from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from SoftDesk.models import Projects, Issues, Comments
from django.contrib.auth.models import User
from SoftDesk.serializers import ProjectsSerializer, IssuesSerializer, CommentsSerializer
from  account.serializers import UserSerializer



class ProjectsViewset(ModelViewSet):
    serializer_class = ProjectsSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Projects.objects.all()
        projects_id = self.request.GET.get('projects_id')
        if projects_id is not None:
            queryset = queryset.filter(projects_id = projects_id)
        return queryset

class IssuesViewset(ModelViewSet):
    serializer_class = IssuesSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Issues.objects.all()
        issues_id = self.request.GET.get('issues_id')
        if issues_id is not None:
            queryset = queryset.filter(issues_id = issues_id)
        return queryset

class UserViewset(ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.all()
        user_id = self.request.GET.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(user_id = user_id)
        return queryset

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def comments_list(request, project_id, issue_id):
    """
    List all comments, or create a new comment.
    """
    get_object_or_404(Projects, id=project_id)
    issue = get_object_or_404(Issues, id=issue_id)

    if request.method == 'GET':
        comment = Comments.objects.filter(issues_id=issue)
        serializer = CommentsSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data.copy()
        data['issue'] = issue.id
        data['author'] = request.user.id

        serializer = CommentsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def comment_detail(request, project_id, issue_id, comment_id):
    """
    Retrieve, update or delete comments.
    """
    get_object_or_404(Projects, id=project_id)
    issue = get_object_or_404(Issues, id=issue_id)
    comment = get_object_or_404(Comments, id=comment_id)

    if request.method == 'GET':
        serializer = CommentsSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data.copy()
        data['issue'] = issue.id
        data['author'] = comment.author_user_id.id

        serializer = CommentsSerializer(comment, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment.delete()
        return Response('Comment successfully deleted.', status=status.HTTP_204_NO_CONTENT)
