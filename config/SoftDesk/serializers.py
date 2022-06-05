from rest_framework.serializers import ModelSerializer
from SoftDesk.models import Projects, Contributors, User, Issues, Comments

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class ProjectsSerializer(ModelSerializer):
    author_user_id = UserSerializer()
    class Meta:
        model = Projects
        fields = ['id', 'title', 'description', 'type', 'author_user_id']

class ContributorsSerializer(ModelSerializer):
    project_id = ProjectsSerializer()
    user_id = UserSerializer()
    class Meta:
        model = Contributors
        fields = ['id', 'user_id', 'project_id', 'permission', 'role']

class IssuesSerializer(ModelSerializer):
    project_id = ProjectsSerializer()
    assignee_user_id = ContributorsSerializer()
    author_user_id = UserSerializer()
    class Meta:
        model = Issues
        fields = ['id', 'title', 'desc', 'tag', 'priority', 'status',
        'created_time', 'author_user_id', 'assignee_user_id', 'project_id']
    
class Comments(ModelSerializer):
    author_user_id = UserSerializer()
    issues_id = IssuesSerializer()
    class Meta:
        model = Comments
        fields = ['id', 'description', 'author_user_id', 'issues_id', 'created_time']