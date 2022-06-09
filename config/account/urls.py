from django.urls import path
from account.views import registration_view
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('signup/', registration_view, name="signup"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
