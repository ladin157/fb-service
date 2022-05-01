import json
import unittest

from test.base import BaseTestCase


def login_user(self):
    return self.client.post(
        '/api/v1/auth/login',
        data=json.dumps(dict(
            email='admin@gmail.com',
            password='1'
        )),
        content_type='application/json'
    )


class TestAuthBlueprint(BaseTestCase):

    def test_user_login(self):
        """ Test for login of registered user """
        with self.client:
            response = login_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue('access_token' in data)
            self.assertTrue(data['access_token'][:36] == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
