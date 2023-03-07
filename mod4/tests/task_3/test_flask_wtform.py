import unittest
from task_1_2.flask_wtform import app


class TestFlaskWtform(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = 'https://localhost/'


    def test_correct(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "test@example.com", "phone": 9999999999, "name": "Kostya", "address": "Lenina", "index": 1})
        assert (response.status_code == 200)
    def test_wrong_email1(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "testexample.com", "phone": 9999999999, "name": "Kostya", "address": "Lenina", "index": 1})
        assert (response.status_code == 400)
    def test_wrong_email2(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "test@examplecom", "phone": 9999999999, "name": "Kostya", "address": "Lenina", "index": 1})
        assert (response.status_code == 400)
    def test_wrong_phone1(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "test@example.com", "phone": "asdsa", "name": "Kostya", "address": "Lenina", "index": 1})
        assert (response.status_code == 400)
    def test_wrong_phone2(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "test@example.com", "phone": 9, "name": "Kostya", "address": "Lenina", "index": 1})
        assert (response.status_code == 400)
    def test_wrong_phone3(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "test@example.com", "phone": 99999999999999999999, "name": "Kostya", "address": "Lenina", "index": 1})
        assert (response.status_code == 400)
    def test_wrong_index(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "test@example.com", "phone": 9999999999, "name": "Kostya", "address": "Lenina", "index": "asdsda"})
        assert (response.status_code == 400)
    def test_empty_email(self):
        response = self.app.post(self.base_url + 'registration',
        data={ "phone": 9999999999, "name": "Kostya", "address": "Lenina", "index": 1})
        assert (response.status_code == 400)
    def test_empty_phone(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "test@example.com",  "name": "Kostya", "address": "Lenina", "index": 1})
        assert (response.status_code == 400)
    def test_empty_name(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "test@example.com", "phone": 9999999999,  "address": "Lenina", "index": 1})
        assert (response.status_code == 400)
    def test_empty_address(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "test@example.com", "phone": 9999999999, "name": "Kostya",  "index": 1})
        assert (response.status_code == 400)
    def test_empty_index(self):
        response = self.app.post(self.base_url + 'registration',
        data={"email": "test@example.com", "phone": 9999999999, "name": "Kostya", "address": "Lenina"})
        assert (response.status_code == 400)
