from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here


class InputTests(APITestCase):
    def test_input_success(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('get-info')
        data = {'date': '20200210'}
        response = self.client.post(url, data, format='json')
        response_text = {
            "Header": {
                "Status": 0,
                "Message": "Successful Operation",
                "MessageCode": 0
            },
            "ContentData": {
                "message": "the information was successfully saved in 2020-02-10-trade.csv"
            }
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_text)

    def test_input_empty(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('get-info')
        data = {'date': '20220215'}
        response = self.client.post(url, data, format='json')
        response_text = {
                "Header": {
                    "Status": 0,
                    "Message": "Not Found",
                    "MessageCode": 3
                },
                "ContentData": {
                    "message": "no information found for 2022-02-15"
                }

        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_text)