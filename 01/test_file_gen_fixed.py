import unittest
from file_generator import function as fn


class TestFile(unittest.TestCase):
    def setUp(self) -> None:
        self.file_name = "./text"

    def test_file(self):
        words = {'ImPlIcIt', 'compLEX'}
        expect = ['Explicit is better than implicit',
                  'Simple is better than complex']
        var = fn(self.file_name, words)
        self.assertEqual(list(var), expect)

    def test_file_without_array_of_words(self):
        words = {}
        expect = []
        var = fn(self.file_name, words)
        self.assertEqual(list(var), expect)

    def test_file_with_file_object_1(self):
        words = {'ImPlIcIt', 'compLEX'}
        expect = ['Explicit is better than implicit',
                  'Simple is better than complex']
        with open(self.file_name) as file_object:
            var = fn(file_object, words)
            self.assertEqual(list(var), expect)

    def test_file_with_file_object_2(self):
        words = {}
        expect = []
        with open(self.file_name) as file_object:
            var = fn(file_object, words)
            self.assertEqual(list(var), expect)

    def test_file_with_file_object_3(self):
        words = {'develop'}
        expect = []
        with open(self.file_name) as file_object:
            var = fn(file_object, words)
            self.assertEqual(list(var), expect)

    def test_file_with_file_object_4(self):
        ''' Должно быть полное совпадение, а нетолько лишь часть слова'''
        words = {'ImpLic'}
        expect = []
        with open(self.file_name) as file_object:
            var = fn(file_object, words)
            self.assertEqual(list(var), expect)
