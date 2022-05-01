import json
import unittest

from requests.auth import HTTPBasicAuth

from test.base import BaseTestCase
import  requests


def search_phone(self):
    return self.client.get(
        '/api/v1/phone/getphonenumber?address=Computer%20History%20Museum%20Mountain%20View',
        content_type='application/json'
    )


class TestPhone(BaseTestCase):

    def test_phone(self):
        """
        The test to get the (formatted) phone number from address.

        Note: There is no
        :return:
        """
        with self.client:
            response = search_phone(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['data']['formatted_phone_number'], '(650) 810-1010')
            self.assertTrue(data['status'] == True)
            self.assertTrue(data['code'] == 200)
            self.assertTrue(data['message'] == 'Success')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
