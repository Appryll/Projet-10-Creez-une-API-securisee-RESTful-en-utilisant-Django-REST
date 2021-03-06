from rest_framework.serializers import ModelSerializer
from SoftDesk.models import Projects, Contributors, Issues, Comments
from rest_framework import serializers

class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"

class ContributorsSerializer(ModelSerializer):
    class Meta:
        model = Contributors
        fields = "__all__"

class IssuesSerializer(ModelSerializer):
    class Meta:
        model = Issues
        fields = "__all__"
    
class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        