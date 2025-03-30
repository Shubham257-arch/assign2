from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class RegisterViewTestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')  # Ensure this name matches your URLconf.
        self.valid_user_data = {
            "username": "testuser",
            "password": "testpassword123",
        }
        self.invalid_user_data = {
            "username": "",  # Empty username should cause failure.
            "password": "short",
        }

    def test_register_user_success(self):
        """Registration should succeed with valid data."""
        response = self.client.post(self.register_url, self.valid_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_register_user_failure(self):
        """Registration should fail with invalid data."""
        response = self.client.post(self.register_url, self.invalid_user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(username="").exists())  # No user should be created.

# Create your tests here.
