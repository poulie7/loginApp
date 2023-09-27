from rest_framework import serializers
from myproject.models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ['article']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email','username',  'password',]

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

