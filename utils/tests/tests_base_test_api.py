from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase


class BaseAPITestCase(APITestCase):
    """
    Base test case for API tests with authentication.
    """

    def setUp(self) -> None:
        self.client: APIClient = APIClient()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        data: dict = {'username': 'test_user','password': 'test_password'}
        self.response_api_token = self.client.post('/auth/token/', data)
        self.token = self.response_api_token.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def get_authenticated_client(self) -> APIClient:
        """
        Returns an authenticated APIClient instance.
        """
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        return client

    def test_authenticated_client(self):
        """
        Test that the client is authenticated after setUp.
        """
        self.assertEqual(self.response_api_token.status_code, 200)