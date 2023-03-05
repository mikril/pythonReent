import unittest
from flaska import app
import flaska

class TestAddCalculate(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        flaska.salarys={2003:{10:15,11:22,9:33}}

    def test_calculate_month(self):
        url = '/calculate/' + '2003/10'
        responseCalculate = self.app.get(url)
        response_text = responseCalculate.data.decode()
        self.assertTrue("15" in response_text.split()[0])
    def test_calculate_year(self):
        url = '/calculate/' + '2003'
        responseCalculate = self.app.get(url)
        response_text = responseCalculate.data.decode()
        self.assertTrue("70" in response_text.split()[0])
    def test_calculate_year_add(self):
        url = '/add/' + '20031015/100'
        responseAdd = self.app.get(url)
        url = '/add/' + '20030808/200'
        responseAdd = self.app.get(url)
        url = '/calculate/' + '2003'
        responseCalculate = self.app.get(url)
        response_text = responseCalculate.data.decode()
        self.assertTrue("370" in response_text.split()[0])
    def test_calculate_empty_year(self):
        flaska.salarys = {}
        url = '/add/'+'20031015/30'
        responseAdd = self.app.get(url)
        url = '/calculate/' + '2003'
        responseCalculate = self.app.get(url)
        response_text = responseCalculate.data.decode()
        self.assertTrue("30" in response_text.split()[0])
    def test_calculate_empty_month(self):
        flaska.salarys = {}
        url = '/add/'+'20031015/30'
        responseAdd = self.app.get(url)
        url = '/calculate/' + '2003/10'
        responseCalculate = self.app.get(url)
        response_text = responseCalculate.data.decode()
        self.assertTrue("30" in response_text.split()[0])
    def test_add(self):
        url = '/add/'+'20041015/30'
        responseAdd = self.app.get(url)
        url = '/calculate/' + '2004'
        responseCalculate = self.app.get(url)
        response_text = responseCalculate.data.decode()

        self.assertTrue("30" in response_text.split()[0])
    def test_correct_date(self):
        url = '/add/'+'abrakodabra/30'
        responseAdd = self.app.get(url)
        response_text = responseAdd.data.decode()
        self.assertTrue("Неправильная дата" in response_text)
    def test_correct_month(self):
        url = '/calculate/' + '2003/3'
        responseCalculate = self.app.get(url)
        response_text = responseCalculate.data.decode()
        self.assertTrue("Такой даты нет" in response_text)
    def test_correct_year(self):
        url = '/calculate/' + '2077'
        responseCalculate = self.app.get(url)
        response_text = responseCalculate.data.decode()
        self.assertTrue("Такого года нет" in response_text)