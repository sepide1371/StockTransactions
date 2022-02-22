from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from oauth2_provider.models import AccessToken, Application, RefreshToken
import datetime
from django.utils import timezone
# Create your tests here


class InputTests(APITestCase):

    def setUp(self):
        self.user = self.setup_user()
        application = Application.objects.create(
            client_id="Th4puZ4Xo83gaRfNhyMTX7kBUSiP1pPYAToivYjq",
            client_type="public",
            client_secret="TzQEQRZx4SOdlk3O4BZDYAxjhgPewB6pXWnEhZ8zSNythcgwZ6DKO79Vs5BIVoKvBcGZQfnTLNB9fo2mrBlLjAADMGqhOcXJwV65NllAHlhevhEQKL5CQ1TQ3RgqBTDb",
            name="test",
            user=self.user,
            authorization_grant_type="password"
        )
        self.access_token = AccessToken.objects.create(
            user=self.user,
            application=application,
            token="WpPFHjsrP15V3UAbfBjWZBUqT2tJ50",
            expires=timezone.now() + datetime.timedelta(seconds=360000),
            scope={'read': 'Read scope'})

        self.refresh_token = RefreshToken.objects.create(
            user=self.user,
            token="CHMcsC9XJXsM0GHjjlZcyXoMKfjtoL",
            access_token=self.access_token,
            application=application)

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='',
            password='test'
        )

    def test_get_info_empty_credential(self):
        client = APIClient()
        url = reverse('get-info')
        data = {'date': '20200210'}
        response = client.post(url, data, format='json')
        response_text = {
            "detail": "Authentication credentials were not provided."}
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, response_text)

    def test_get_info_wrong_credential(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           '123456789')
        url = reverse('get-info')
        data = {'date': '20200210'}
        response = client.post(url, data, format='json')
        response_text = {
            "detail": "Authentication credentials were not provided."}
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, response_text)

    def test_get_info_input_success(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           self.access_token.token)
        url = reverse('get-info')
        data = {'date': '20200210'}
        response = client.post(url, data, format='json')
        response_text = {
            "Header": {
                "Status": 200,
                "Message": "Successful Operation",
                "MessageCode": 0
            },
            "ContentData": {
                "message": "the information was successfully saved in 2020-02-10-trade.csv"
            }
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_text)

    def test_get_info_input_empty(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           self.access_token.token)
        url = reverse('get-info')
        data = {'date': '20220215'}
        response = client.post(url, data, format='json')
        response_text = {
            "Header": {
                "Status": 200,
                "Message": "Not Found",
                "MessageCode": 3
            },
            "ContentData": {
                "message": "no information found for 2022-02-15"
            }
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_text)

    def test_get_info_check_date(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           self.access_token.token)
        url = reverse('get-info')
        data = {'date': '2022-02-15'}
        response = client.post(url, data, format='json')
        response_text = {
            "Header": {
                "Status": 400,
                "Message": "Input Error",
                "MessageCode": 2
            },
            "ContentData": {
                "errors": {
                    "date": [
                        "Date has wrong format. Use one of these formats instead: YYYYMMDD."
                    ]
                }
            }
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_text)

    def test_get_info_empty_body(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           self.access_token.token)
        url = reverse('get-info')
        data = {}
        response = client.post(url, data, format='json')
        response_text = {
            "Header": {
                "Status": 400,
                "Message": "Input Error",
                "MessageCode": 2
            },
            "ContentData": {
                "errors": {
                    "date": [
                        "This field is required."
                    ]
                }
            }
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_text)

    def test_trade_info_empty_credential(self):
        client = APIClient()
        url = reverse('trade-info')
        data = {'date': '20200210'}
        response = client.post(url, data, format='json')
        response_text = {
            "detail": "Authentication credentials were not provided."}
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, response_text)

    def test_trade_info_wrong_credential(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           '123456789')
        url = reverse('trade-info')
        data = {'date': '20200210'}
        response = client.post(url, data, format='json')
        response_text = {
            "detail": "Authentication credentials were not provided."}
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, response_text)

    def test_trade_info_input_success(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           self.access_token.token)
        url = reverse('trade-info')
        data = {'date': '20220214'}
        response = client.post(url, data, format='json')
        response_text = {
            "Header": {
                "Status": 200,
                "Message": "Successful Operation",
                "MessageCode": 0
            },
            "ContentData": {
                "num_items": 6020,
                "pTranSUM": 12154158.0,
                "pTranAVG": 2018.9631229235881,
                "qTitTranSUM": 208622122,
                "qTitTranAVG": 34654.83754152824
            }
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_text)

    def test_trade_info_input_empty(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           self.access_token.token)
        url = reverse('trade-info')
        data = {'date': '20220215'}
        response = client.post(url, data, format='json')
        response_text = {
            "Header": {
                "Status": 200,
                "Message": "Not Found",
                "MessageCode": 3
            },
            "ContentData": {
                "message": "file not found for 2022-02-15"
            }
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_text)

    def test_trade_info_check_date(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           self.access_token.token)
        url = reverse('trade-info')
        data = {'date': '2022-02-15'}
        response = client.post(url, data, format='json')
        response_text = {
            "Header": {
                "Status": 400,
                "Message": "Input Error",
                "MessageCode": 2
            },
            "ContentData": {
                "errors": {
                    "date": [
                        "Date has wrong format. Use one of these formats instead: YYYYMMDD."
                    ]
                }
            }
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_text)

    def test_trade_info_empty_body(self):

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' +
                           self.access_token.token)
        url = reverse('trade-info')
        data = {}
        response = client.post(url, data, format='json')
        response_text = {
            "Header": {
                "Status": 400,
                "Message": "Input Error",
                "MessageCode": 2
            },
            "ContentData": {
                "errors": {
                    "date": [
                        "This field is required."
                    ]
                }
            }
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_text)
