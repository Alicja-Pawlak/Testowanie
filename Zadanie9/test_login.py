import unittest
import login
import json
import requests

class TestLogin(unittest.TestCase):

    def test_valid_login(self):

        loginObj = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        responseObj = {
            "token":"QpwL5tke4Pnpja7X4"
        }

        response = requests.post(login.gl_url() + "/api/login", data = loginObj)
        token = json.loads(response.text)

        self.assertEqual(token, responseObj)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':  
    unittest.main()  