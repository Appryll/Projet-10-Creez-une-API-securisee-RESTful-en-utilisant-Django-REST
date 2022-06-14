from rest_framework.response import Response
from account.serializers import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User


@api_view(['GET', 'POST', ])
def registration_view(request):

	if request.method == 'POST':
		serializer = UserSerializer (data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	
	if request.method == 'GET':
		users = User.objects.all()
		serializer =UserSerializer(users, many=True)
		return Response(serializer.data)
		