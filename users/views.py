from contextvars import Token
from urllib import request

import username
from django.contrib.auth.models import User  # Correct import
from django.contrib.auth.views import LoginView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)  # Correct spelling for permission_classes


class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({"error": "Username and password are required"}, status=400)
    user = User.objects.filter(username=username).first()
    if not user or not user.check_password(password):
        return Response({"error": "Invalid username or password"}, status=401)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key}, status=200)
