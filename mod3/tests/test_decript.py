import unittest
from decript import decript

class TestDecript(unittest.TestCase):
    def test_get_word(self):
        outWord=["абра-кадабра.", "абраа..-кадабра", "абраа..-.кадабра", "абра--..кадабра", "абрау...-кадабра"]

        for word in outWord:
            with self.subTest(word=word):
                self.assertEqual(decript(word), "абра-кадабра")
    def test_one_Empty(self):
        ouEmpty=["абра.........", "1.......................", "."]
        for word in ouEmpty:
            with self.subTest(word=word):
                self.assertEqual(decript(word), "")

    def test_out_a(self):
        inputWord = "абр......a."
        expected_res = "a"
        function_res = decript(inputWord)
        self.assertEqual(expected_res, function_res)
    def test_out_23(self):
        inputWord = "1..2.3"
        expected_res = "23"
        function_res = decript(inputWord)
        self.assertEqual(expected_res, function_res)