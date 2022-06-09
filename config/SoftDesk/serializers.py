from rest_framework.serializers import ModelSerializer
from SoftDesk.models import Projects, Contributors, User, Issues, Comments
from account.serializers import UserSerializer

class ProjectsSerializer(ModelSerializer):
    author_user_id = UserSerializer() #imbrique les serializers
    class Meta:
        model = Projects
        fields = "__all__"

class ContributorsSerializer(ModelSerializer):
    project_id = ProjectsSerializer()
    user_id = UserSerializer()
    class Meta:
        model = Contributors
        fields = "__all__"

class IssuesSerializer(ModelSerializer):
    # project_id = ProjectsSerializer()
    # assignee_user_id = ContributorsSerializer()
    # author_user_id = UserSerializer()
    class Meta:
        model = Issues
        fields = "__all__"
    
class CommentsSerializer(ModelSerializer):
    # author_user_id = UserSerializer()
    # issues_id = IssuesSerializer()
    class Meta:
        model = Comments
        fields = "__all__"
        