from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

User = get_user_model()


class SignUpAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse("signup_api")

    def test_signup_user(self):
        user_data = {
            "first_name": "tester",
            "last_name": "tester",
            "email": "test@example.com",
            "password": "testpassword",
        }

        response = self.client.post(self.signup_url, user_data, format="json")
        # print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "tester")
        self.assertEqual(response.data["last_name"], "tester")
        self.assertEqual(response.data["email"], "test@example.com")

    def test_signup_invalid_data(self):
        invalid_user_data = {
            "first_name": "",  # Invalid username
            "email": "invalid_email",  # Invalid email
            "password": "short",  # Invalid password
        }

        response = self.client.post(self.signup_url, invalid_user_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse("login_api")
        self.user_data = {"email": "test@example.com", "password": "testpassword"}
        self.user = User.objects.create_user(**self.user_data)
        self.token = Token.objects.create(user=self.user)

    def test_login_successful(self):
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
        self.assertEqual(response.data["message"], "Login successful!")

    def test_login_invalid_credentials(self):
        invalid_data = {"email": "test@wrongemail.com", "password": "wrongpassword"}
        response = self.client.post(self.login_url, invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["message"], "Invalid email or password")

    def test_login_with_existing_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
        self.assertEqual(response.data["message"], "Login successful!")


class LogoutAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.logout_url = reverse("logout_api")
        self.user_data = {"email": "test@example.com", "password": "testpassword"}
        self.user = User.objects.create_user(**self.user_data)
        self.token = Token.objects.create(user=self.user)

    def test_logout_successful(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        response = self.client.post(self.logout_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Logout successful!")

        # Verify that the token has been deleted
        with self.assertRaises(Token.DoesNotExist):
            Token.objects.get(key=self.token.key)

    def test_logout_without_token(self):
        response = self.client.post(self.logout_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data["detail"], "Authentication credentials were not provided."
        )
