from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    Username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Note
        fields = ['id ,title ,content ,Username' ,'user']
