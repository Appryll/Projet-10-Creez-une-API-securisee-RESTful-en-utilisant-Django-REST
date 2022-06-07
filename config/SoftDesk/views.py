from rest_framework.viewsets import ModelViewSet

from SoftDesk.models import Projects, Issues
from SoftDesk.serializers import ProjectsSerializer, IssuesSerializer


class ProjectsViewset(ModelViewSet):

    serializer_class = ProjectsSerializer

    def get_queryset(self):
        queryset = Projects.objects.all()
        projects_id = self.request.GET.get('projects_id')
        if projects_id is not None:
            queryset = queryset.filter(projects_id = projects_id)
        return queryset

class IssuesViewset(ModelViewSet):

    serializer_class = IssuesSerializer

    def get_queryset(self):
        queryset = Issues.objects.all()
        issues_id = self.request.GET.get('issues_id')
        if issues_id is not None:
            queryset = queryset.filter(issues_id = issues_id)
        return queryset
