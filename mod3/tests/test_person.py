import unittest
import person
class TestAddCalculate(unittest.TestCase):
    def setUp(self):
        self.person=person.Person("Kostay",2003,"Visotsky")

    def test_get_age(self):
        self.assertTrue(self.person.get_age()==20)

    def test_get_name(self):
        self.assertTrue(self.person.get_name()=="Kostay")

    def test_set_name(self):
        self.person.set_name("Jhon")
        self.assertTrue(self.person.name=="Jhon")

    def test_set_address(self):
        self.person.set_address("walk street")
        self.assertTrue(self.person.address=="walk street")

    def test_get_address(self):
        self.assertTrue(self.person.get_address()=="Visotsky")

    def test_is_homeless(self):
        self.assertTrue(self.person.is_homeless()==Falsee)
