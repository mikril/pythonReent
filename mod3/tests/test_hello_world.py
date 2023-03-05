import unittest
from flaska import app
from freezegun import freeze_time

class TestHello(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'
    def test_hello_name(self):
        username = 'username'
        response = self.app.get(self.base_url + username)

        response_text = response.data.decode()

        self.assertTrue(username in response_text)

    @freeze_time("2012-01-14")
    def test_hello_correct_day(self):
        username = 'username'
        response = self.app.get(self.base_url + username)

        response_text = response.data.decode().split(".")[1]
        self.assertTrue("субботы" in response_text)

    @freeze_time("2012-01-16")
    def test_hello_correct_fake_name(self):
        username = 'Хорошей среды'
        response = self.app.get(self.base_url + username)

        response_text = response.data.decode().split(".")[1]
        self.assertTrue("понедельника" in response_text)
        self.assertFalse("среды" in response_text)

