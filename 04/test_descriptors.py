import unittest
from descriptors import Data


class TestDescriptor(unittest.TestCase):

    def test_integer(self):

        arr1 = [1.1, {1, 2, 3, 4}, {'se': 1}, (1, 2), 'type']
        var = Data()
        with self.assertRaises(TypeError):
            for temp in arr1:
                var.num = temp

        arr2 = [-11, 0, 2, 3, -4]
        for temp in arr2:
            var.num = temp
            self.assertEqual(var.num, temp)
            self.assertIsInstance(var.num, int)

    def test_positive_integer(self):

        arr1 = [1.1, {1, 2, 3, 4}, {'se': 1}, (1, 2), 'type']
        var = Data()
        with self.assertRaises(TypeError):
            for temp in arr1:
                var.price = temp

        arr2 = [1, 2, 3, 4]
        for temp in arr2:
            var.price = temp
            self.assertEqual(var.price, temp)
            self.assertTrue(var.price > 0)
            self.assertIsInstance(var.price, int)

    def test_string(self):

        arr1 = [1.1, {1, 2, 3, 4}, {'se': 1}, (1, 2), 1]
        var = Data()
        with self.assertRaises(TypeError):
            for temp in arr1:
                var.name = temp

        arr2 = ['aa', 'qwe', '']
        for temp in arr2:
            var.name = temp
            self.assertEqual(var.name, temp)
            self.assertIsInstance(var.name, str)
