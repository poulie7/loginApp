from rest_framework.views import APIView
from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, authenticate, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from  django.contrib.auth.views import LoginView

from myproject.models import Article
from .serializer import ArticleSerializer, UserSerializer, LoginSerializer
from django.contrib.auth.models import User


class ArticleView(generics.ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	authentication_classes = [SessionAuthentication, ]
	permission_classes = [IsAuthenticated, ]


class RegisterView(generics.CreateAPIView):
	serializer_class = UserSerializer

	def post(self, request):
		serializer = UserSerializer(data=request.data)

		if serializer.is_valid():
			first_name = serializer.validated_data.get('first_name')
			last_name = serializer.validated_data.get('last_name')
			email = serializer.validated_data.get('email')
			username = serializer.validated_data.get('username')
			password = serializer.validated_data.get('password')

			user = User.objects.create_user(
				first_name=first_name,
				last_name=last_name,
				email=email,
				username=username,
				password=password
			)
			user.save()

			return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
	serializer_class = LoginSerializer
	authentication_classes = [SessionAuthentication, ]

	def post(self, request):
		if request.user.is_authenticated:
			return Response({'message': 'User is already logged in'}, status=status.HTTP_200_OK)
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			email = serializer.validated_data.get('username')
			password = serializer.validated_data.get('password')
			user = authentication.authenticate(request, username=email, password=password)

			if user is not None:
				login(request, user)
				response = Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
				return response
			else:
				return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
		else:
			# If the serializer is not valid, return validation errors
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

	def get(self, request):
		logout(request)
		request.session.flush()
		return Response({"message": "logged out"})
