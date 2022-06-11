"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from SoftDesk.views import ProjectsViewset, IssuesViewset, UserViewset, comments_list, comment_detail

router = routers.SimpleRouter()
router.register('projects', ProjectsViewset, basename='projects')

user_router = routers.NestedSimpleRouter(router, 'projects', lookup='projects')
user_router.register('user', UserViewset, basename='projects-user')

issues_router = routers.NestedSimpleRouter(router, 'projects', lookup='projects')
issues_router.register('issues', IssuesViewset, basename='projects-issues')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), #log in http://127.0.0.1:8000/
    path('', include('account.urls')),

    path('', include(router.urls)),
    path('', include(user_router.urls)),
    path('', include(issues_router.urls)),

    path('projects/<int:project_id>/issues/<int:issue_id>/comments/', comments_list),    
    path('projects/<int:project_id>/issues/<int:issue_id>/comments/<int:comment_id>/', comment_detail),    
]
