from django.contrib.auth.models import User  # Correct import
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)  # Correct spelling for permission_classes
