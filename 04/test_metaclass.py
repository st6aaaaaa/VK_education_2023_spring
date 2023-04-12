import unittest
import metaclass


def func1(var):
    return 2*var


class TestMetaClass(unittest.TestCase):
    def setUp(self):
        self.class_var = metaclass.CustomClass(1, 2)
        self.class_var.var = 12
        self.class_var.function1 = func1
        self.class_var.function2 = lambda x: x.upper()
        self.class_var._v1 = 12

    def test_class(self):
        self.assertEqual(self.class_var.__dict__['_custom_protect'], 1)
        self.assertEqual(self.class_var.__dict__['__custom_private'], 2)
        self.assertEqual(self.class_var.__dict__['custom_val'], 99)
        self.assertEqual(self.class_var.__dict__['custom_var'], 12)
        self.assertEqual(self.class_var.__dict__['custom_function1'](2), 4)
        self.assertEqual(str(self.class_var), "Custom_by_metaclass")
        self.assertEqual(
                         repr(self.class_var),
                         "testing __repr__ of CustomClass")
        self.assertEqual(
                         self.class_var.__dict__['custom_function2']('aaa'),
                         'AAA')
        self.assertEqual(self.class_var.__dict__['_custom_v1'], 12)
        self.assertEqual(metaclass.CustomClass.__dict__['custom_x'], 50)

        with self.assertRaises(KeyError):
            self.assertEqual(self.class_var.__dict__['_protect'], 1)
            self.assertEqual(self.class_var.__dict__['__private'], 2)
            self.assertEqual(self.class_var.__dict__['val'], 99)
            self.assertEqual(self.class_var.__dict__['var'], 12)
            self.assertEqual(self.class_var.__dict__['function1'](2), 4)
            self.assertEqual(
                             self.class_var.__dict__['function2']('aaa'),
                             'AAA')
            self.assertEqual(self.class_var.__dict__['_v1'], 12)
            self.assertEqual(metaclass.CustomClass.__dict__['x'], 50)

        with self.assertRaises(AttributeError):
            self.assertEqual(self.class_var.line(), 100)
            self.assertEqual(metaclass.CustomClass.x, 50)
