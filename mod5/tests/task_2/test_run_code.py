import unittest
from task_2.run_code import app


class TestRunCode(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = 'https://localhost/'

    def test_time_end(self):
        response = self.app.post(self.base_url + 'run_code',data={"code": "import time; time.sleep(2)","timeout":1})
        assert (response.text.split(": ")[-1]=="True")
    def test_not_correct_data(self):
        response = self.app.post(self.base_url + 'run_code',data={"code": "print(hello)","timeout":31})
        assert (response.status_code==400)
    def test_shell(self):
        response = self.app.post(self.base_url + 'run_code',data={"code": 'print(hello)"; echo "hacked ',"timeout":31})
        assert (not("hacked" in response.text))