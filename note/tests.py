from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Note

class NoteViewManualTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test123')
        self.token = Token.objects.create(user=self.user)
        self.url = '/note/'  # Using the direct RESTful endpoint

    def test_create_note_successfully(self):
        print("✅ note.tests.py loaded")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            "title": "My Note",
            "content": "This is a test note."
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("note_id", response.data)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.first().title, "My Note")

    def test_create_note_missing_fields(self):
        print("✅ note.tests.py missing fields")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_unauthorized_note_creation(self):
        print("✅ note.tests.py unauthorized")
        response = self.client.post(self.url, {"title": "x", "content": "y"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
