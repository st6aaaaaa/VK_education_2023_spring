import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def test_radd(self):
        items = [([1, 2, 3], CustomList([1, 2]), CustomList([2, 4, 3])),
                 ([1, 2, 3], CustomList([1, 2, 3]), CustomList([2, 4, 6])),
                 ([1, 2], CustomList([1, 2, 3]), CustomList([2, 4, 3]))
                 ]
        tmp_arr = [item[0] + item[1] for item in items]
        for i in range(len(items)):
            self.assertEqual(list(tmp_arr[i]), list(items[i][2]))

        self.assertEqual(items[0][0], [1, 2, 3])
        self.assertEqual(items[1][0], [1, 2, 3])
        self.assertEqual(items[2][0], [1, 2])

        self.assertEqual(items[0][1], CustomList([1, 2]))
        self.assertEqual(items[1][1], CustomList([1, 2, 3]))
        self.assertEqual(items[2][1], CustomList([1, 2, 3]))

    def test_add(self):
        items = [(CustomList([1, 2, 3]), CustomList([1, 2]),
                  CustomList([2, 4, 3])),
                 (CustomList([1, 2, 3]), CustomList([1, 2, 3]),
                  CustomList([2, 4, 6])),
                 (CustomList([1, 2]), CustomList([1, 2, 3]),
                  CustomList([2, 4, 3]))
                 ]
        tmp_arr = [item[0] + item[1] for item in items]
        for i in range(len(items)):
            self.assertEqual(list(tmp_arr[i]), list(items[i][2]))

        self.assertEqual(items[0][0], CustomList([1, 2, 3]))
        self.assertEqual(items[1][0], CustomList([1, 2, 3]))
        self.assertEqual(items[2][0], CustomList([1, 2]))

        self.assertEqual(items[0][1], CustomList([1, 2]))
        self.assertEqual(items[1][1], CustomList([1, 2, 3]))
        self.assertEqual(items[2][1], CustomList([1, 2, 3]))

    def test_sub(self):
        items = [(CustomList([1, 2, 3]), CustomList([1, 2, 0, 0]),
                  CustomList([0, 0, 3, 0])),
                 (CustomList([1, 2, 3]), CustomList([1, 2, 4]),
                  CustomList([0, 0, -1])),
                 (CustomList([1, 3]), CustomList([1, 2, 3]),
                  CustomList([0, 1, -3]))
                 ]
        tmp_arr = [item[0] - item[1] for item in items]
        for i in range(len(items)):
            self.assertEqual(list(tmp_arr[i]), list(items[i][2]))

        self.assertEqual(items[0][0], CustomList([1, 2, 3]))
        self.assertEqual(items[1][0], CustomList([1, 2, 3]))
        self.assertEqual(items[2][0], CustomList([1, 3]))

        self.assertEqual(items[0][1], CustomList([1, 2]))
        self.assertEqual(items[1][1], CustomList([1, 2, 4]))
        self.assertEqual(items[2][1], CustomList([1, 2, 3]))

    def test_rsub(self):
        items = [([1, 2, 3], CustomList([1, 2]), CustomList([0, 0, 3])),
                 ([1, 2, 3, 0, 0], CustomList([1, 2, 4]),
                  CustomList([0, 0, -1, 0, 0])),
                 ([1, 3], CustomList([1, 2, 3]), CustomList([0, 1, -3]))
                 ]
        tmp_arr = [item[0] - item[1] for item in items]
        for i in range(len(items)):
            self.assertEqual(list(tmp_arr[i]), list(items[i][2]))

        self.assertEqual(items[0][0], [1, 2, 3])
        self.assertEqual(items[1][0], [1, 2, 3, 0, 0])
        self.assertEqual(items[2][0], [1, 3])

        self.assertEqual(items[0][1], CustomList([1, 2]))
        self.assertEqual(items[1][1], CustomList([1, 2, 4]))
        self.assertEqual(items[2][1], CustomList([1, 2, 3]))

    def test_str(self):
        self.assertEqual(CustomList([1, 2, 3]).__str__(), "[1, 2, 3] 6")
        self.assertEqual(CustomList([1]).__str__(), "[1] 1")

    def test_eq(self):
        self.assertTrue(CustomList([1, 2, 4]).__eq__([2, 2, 3]))
        self.assertFalse(list([1, 2, 4]).__eq__(list([2, 2, 3])))

        self.assertFalse(CustomList([1]).__eq__([1, 2, 3]))

        self.assertTrue(all([CustomList([1, 2, 3]).__eq__([1, 2, 3]),
                             list([1, 2, 3]).__eq__(list([1, 2, 3]))])
                        )

    def test_lt(self):
        self.assertTrue(CustomList([1, 2, 3]).__lt__([1, 2, 4]))
        self.assertTrue(CustomList([1]).__lt__([1, 2, 3]))

    def test_le(self):
        self.assertTrue(CustomList([1, 2, 3]).__le__([1, 7, 4]))
        self.assertTrue(CustomList([1]).__le__([1, -1, 1]))

    def test_ge(self):
        self.assertTrue(CustomList([1, 2, 3]).__ge__([1, -7, 4]))
        self.assertTrue(CustomList([1]).__ge__([1]))

    def test_gt(self):
        self.assertTrue(CustomList([1, 2, 3]).__gt__([1, -7, 4]))
        self.assertTrue(CustomList([1]).__gt__([-1]))

    def test_ne(self):
        self.assertTrue(CustomList([1, 2, 3]).__ne__([1, -7, 4]))
        self.assertTrue(CustomList([1]).__ne__([-1]))
        
        
