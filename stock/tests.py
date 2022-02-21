from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here


class InputTests(APITestCase):
    def test_get_info_input_success(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('get-info')
        data = {'date': '20200210'}
        response = self.client.post(url, data, format='json')
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
        """
        Ensure we can create a new account object.
        """
        url = reverse('get-info')
        data = {'date': '20220215'}
        response = self.client.post(url, data, format='json')
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
        """
        Ensure we can create a new account object.
        """
        url = reverse('get-info')
        data = {'date': '2022-02-15'}
        response = self.client.post(url, data, format='json')
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
        """
        Ensure we can create a new account object.
        """
        url = reverse('get-info')
        data = {}
        response = self.client.post(url, data, format='json')
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


    def test_trade_info_input_success(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('trade-info')
        data = {'date': '20220214'}
        response = self.client.post(url, data, format='json')
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
        """
        Ensure we can create a new account object.
        """
        url = reverse('trade-info')
        data = {'date': '20220215'}
        response = self.client.post(url, data, format='json')
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
        """
        Ensure we can create a new account object.
        """
        url = reverse('trade-info')
        data = {'date': '2022-02-15'}
        response = self.client.post(url, data, format='json')
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
        """
        Ensure we can create a new account object.
        """
        url = reverse('trade-info')
        data = {}
        response = self.client.post(url, data, format='json')
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