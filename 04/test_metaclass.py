import unittest
from metaclass import CustomClass


def func1(var):
    return 2 * var


class TestMetaClass(unittest.TestCase):
    def setUp(self):
        self.class_var = CustomClass(1, 2)
        self.class_var.var = 12
        self.class_var.function1 = func1
        self.class_var.function2 = lambda x: x.upper()
        self.class_var._v1 = 12

    def test_class(self):
        self.assertFalse(hasattr(self.class_var, '_protect'))
        self.assertFalse(hasattr(self.class_var, '__private'))
        self.assertFalse(hasattr(self.class_var, 'val'))
        self.assertFalse(hasattr(self.class_var, 'function1'))
        self.assertFalse(hasattr(self.class_var, 'function2'))
        self.assertFalse(hasattr(self.class_var, '_v1'))
        self.assertFalse(hasattr(CustomClass, 'x'))
        self.assertFalse(hasattr(CustomClass, 'line'))

        self.assertTrue(hasattr(self.class_var, '_custom_protect'))
        self.assertTrue(hasattr(self.class_var, '__custom_private'))
        self.assertTrue(hasattr(self.class_var, 'custom_val'))
        self.assertTrue(hasattr(self.class_var, 'custom_function1'))
        self.assertTrue(hasattr(self.class_var, 'custom_function2'))
        self.assertTrue(hasattr(self.class_var, '_custom_v1'))
        self.assertTrue(hasattr(CustomClass, 'custom_x'))
        self.assertTrue(hasattr(CustomClass, 'custom_line'))

        self.assertTrue(getattr(self.class_var, '_custom_protect'), 1)
        self.assertTrue(getattr(self.class_var, '__custom_private'), 2)
        self.assertTrue(getattr(self.class_var, 'custom_val'), 99)
        self.assertTrue(getattr(self.class_var, 'custom_var'), 12)
        self.assertTrue(getattr(self.class_var, 'custom_function1')(2), 4)
        self.assertTrue(getattr(self.class_var, '__str__')(),
                        "Custom_by_metaclass")

        self.assertEqual(repr(self.class_var),
                         "testing __repr__ of CustomClass")
        self.assertTrue(getattr(self.class_var, 'custom_function2')('aaa'),
                        'AAA')

        self.assertTrue(getattr(self.class_var, '_custom_v1'), 12)
        self.assertTrue(getattr(CustomClass, 'custom_x'), 50)

        self.assertTrue(hasattr(CustomClass, 'custom_x'))
        self.assertTrue(hasattr(CustomClass, '__custom_hello'))
        self.assertTrue(hasattr(CustomClass, '_custom_var'))
        self.assertTrue(hasattr(CustomClass, 'custom_line'))

        self.assertFalse(hasattr(CustomClass, 'x'))
        self.assertFalse(hasattr(CustomClass, '__hello'))
        self.assertFalse(hasattr(CustomClass, '_var'))
        self.assertFalse(hasattr(CustomClass, 'line'))

        for i, j in zip(['x', '_var', '__hello'], [50, 12, 13]):
            with self.assertRaises(AttributeError):
                self.assertEqual(getattr(CustomClass, i), j)

        with self.assertRaises(AttributeError):
            self.assertEqual(CustomClass.x, 50)

        with self.assertRaises(AttributeError):
            self.assertEqual(CustomClass._var, 12)

        with self.assertRaises(AttributeError):
            self.assertEqual(CustomClass.__hello, 13)

        self.assertEqual(CustomClass.custom_x, 50)
        self.assertEqual(CustomClass._custom_var, 12)
        self.assertEqual(getattr(CustomClass, '__custom_hello'), 13)

        self.assertEqual(self.class_var._custom_protect, 1)
        self.assertEqual(getattr(self.class_var, '__custom_private'), 2)
        self.assertEqual(self.class_var.custom_val, 99)
        self.assertEqual(self.class_var.custom_function1(2), 4)
        self.assertEqual(self.class_var.custom_function2('a'), 'A')
        self.assertEqual(self.class_var._custom_v1, 12)

        with self.assertRaises(AttributeError):
            self.assertEqual(self.class_var._protect, 1)

        with self.assertRaises(AttributeError):
            self.assertEqual(self.class_var.val, 99)

        with self.assertRaises(AttributeError):
            self.assertEqual(self.class_var.function1(2), 4)

        with self.assertRaises(AttributeError):
            self.assertEqual(self.class_var.function2('a'), 'A')

        with self.assertRaises(AttributeError):
            self.assertEqual(self.class_var._v1, 12)
            
