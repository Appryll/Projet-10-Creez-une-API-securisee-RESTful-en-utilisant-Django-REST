from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	username = serializers.CharField()
	first_name = serializers.CharField()
	last_name = serializers.CharField()
	email = serializers.EmailField()
	password = serializers.CharField()
	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)


	def create(self, validate_data):
		account = User()
		account.username = validate_data.get('username')
		account.first_name = validate_data.get('first_name')
		account.last_name = validate_data.get('last_name')
		account.email = validate_data.get('email')

		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		
		account.set_password(validate_data.get('password'))
		account.save()
		return account

	def validate_email(self, data):
		mail = User.objects.filter(email = data)
		if len(mail) != 0:
			raise serializers.ValidationError("This email already exists. Enter a new email")
		else:
			return data

	def validate_username(self, data):
		user = User.objects.filter(username = data)
		if len(user) != 0:
			raise serializers.ValidationError("This username already exists. Enter a new username")
		else:
			return data

# from rest_framework import serializers

# from SoftDesk.models import User


# # class LoginSerializer(serializers.ModelSerializer):
# # 	class Meta:
# # 		model = Account
# # 		fields = ['email', 'password',]

# # 		extra_kwargs = {'password': {'write_only': True}}

# # 	def validate(self, data):
# # 		password = data.get('password')
# # 		email = data.get('email')


# class RegistrationSerializer(serializers.ModelSerializer):

# 	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

# 	class Meta:
# 		model = User
# 		fields = ['email', 'first_name', 'last_name', 'password', 'password2']
# 		extra_kwargs = {
# 				'password': {'write_only': True},
# 		}	


# 	def	save(self):

# 		account = User(
# 					email=self.validated_data['email'],
# 					first_name=self.validated_data['first_name'],
#                     last_name= self.validated_data['last_name']
# 				)
# 		password = self.validated_data['password']
# 		password2 = self.validated_data['password2']
# 		if password != password2:
# 			raise serializers.ValidationError({'password': 'Passwords must match.'})
# 		account.set_password(password)
# 		account.save()
# 		return account