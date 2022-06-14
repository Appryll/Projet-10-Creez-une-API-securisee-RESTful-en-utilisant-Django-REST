from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from SoftDesk.models import Projects, Issues, Comments, Contributors
from SoftDesk.serializers import (ProjectsSerializer, ContributorsSerializer, 
                                    IssuesSerializer, CommentsSerializer)
from SoftDesk.permissions import (PermissionsViewContributor, PermissionsProjectAuthor, 
                                    PermissionsCommentAuthor, 
                                    PermissionsContributorAuthorProjet, 
                                    PermissionsIssueAuthor)


@api_view(['GET', 'POST']) 
@permission_classes([PermissionsViewContributor, IsAuthenticated])
def project_list(request):
    if request.method == 'GET':
        projects = Projects.objects.filter(author_user_id=request.user.id) | Projects.objects.filter(contributor__user_id=request.user.id)
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data.copy()
        data['author_user_id'] = request.user.id

        serializer = ProjectsSerializer(data=data)
        if serializer.is_valid():
            project = serializer.save()
            Contributors.objects.create(user_id=request.user, project_id=project, role='L\'AUTEUR')
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([PermissionsProjectAuthor, IsAuthenticated])
def project_detail(request, project_id):
    project = get_object_or_404(Projects, id=project_id)

    if request.method == 'GET':
        serializer = ProjectsSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = request.data.copy()
        data['author_user_id'] = project.author_user_id.id

        serializer = ProjectsSerializer(project, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response('Project deleted successfully!', status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def contributor_list(request, project_id):
    project = get_object_or_404(Projects, id=project_id)

    if request.method == 'GET':
        contributors = Contributors.objects.filter(project_id=project)
        serializer = ContributorsSerializer(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST': 
        #seul l'auteur du projet peut ajouter des contributeurs
        if request.user.id == project.author_user_id.id:
            data = request.data.copy()
            data['project_id'] = project.id

            serializer = ContributorsSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('You do not have permission to add contributors to the project. Only the author of the project has that right.')


@api_view(['DELETE'])
@permission_classes([PermissionsContributorAuthorProjet, IsAuthenticated])
def contributor_detail(request, contributor_id, project_id):
    contributor = get_object_or_404(Contributors, id=contributor_id)
    project = get_object_or_404(Projects, id=project_id)

    if request.method == 'DELETE':
        contributor.delete()
        return Response('Contributor deleted successfully!', status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def issue_list(request, project_id):
    """
    List all issues, or create a new issue.
    Permissions: Only authenticated users can access.
    """
    project = get_object_or_404(Projects, id=project_id)

    if request.method == 'GET':
        issues = Issues.objects.filter(project_id=project_id)
        serializer = IssuesSerializer(issues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data.copy()
        data['project_id'] = project_id
        data['author_user_id'] = request.user.id
 
        serializer = IssuesSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
@permission_classes([PermissionsIssueAuthor, IsAuthenticated])
def issue_detail(request, project_id, issue_id):
    """
    Retrieve, update or delete issues.
    Permissions:An issue can only be updated or deleted by its author, but it is remain visible to all contributors to the project.
    """
    project = get_object_or_404(Projects, id=project_id)
    issue = get_object_or_404(Issues, id=issue_id)

    if request.method == 'PUT':
        data = request.data.copy()
        data['project_id'] = project.id
        data['author_user_id'] = issue.author_user_id.id

        serializer = IssuesSerializer(issue, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        issue.delete()
        return Response('Issue successfully deleted.', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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
@permission_classes([PermissionsCommentAuthor, IsAuthenticated])
def comment_detail(request, project_id, issue_id, comment_id):
    """
    Retrieve, update or delete comments.
    Permissions: Comments should be visible to all project contributors and the project manager, but only their author can update or delete them.
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
