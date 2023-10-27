from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


# Test cases for authentication views
class TestAuthViews(TestCase):
    def setUp(self):
        # Set up test data and URLs
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'password': 'uwyeruiwhfuiwhfiu232'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.refresh_token = RefreshToken.for_user(self.user)
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.logout_url = reverse('logout')

    def test_obtain_token_pair(self):
        # Test obtaining a token pair by logging in
        response = self.client.post(
            self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_registration(self):
        # Test user registration
        new_user_data = {
            'username': 'newuser',
            'password1': 'uwyeruiwhfuiwhfiu232',
            'password2': 'uwyeruiwhfuiwhfiu232',
            'email': 'testuser@email.com',
            'first_name': 'NewUser',
            'last_name': 'NewUserLast'
        }
        response = self.client.post(
            self.register_url, new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_logout(self):
        # Test user logout with a valid refresh token
        refresh_token_data = {'refresh_token': str(self.refresh_token)}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            self.logout_url, refresh_token_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_logout_without_refresh_token(self):
        # Test user logout without providing a refresh token
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.logout_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_logout_with_invalid_refresh_token(self):
        # Test user logout with an invalid refresh token
        invalid_token_data = {'refresh_token': 'invalid_token'}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            self.logout_url, invalid_token_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
