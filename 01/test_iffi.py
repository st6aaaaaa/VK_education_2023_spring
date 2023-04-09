from unittest.mock import patch
from unittest import mock
import unittest
import iffi


class TestIffi(unittest.TestCase):
    def setUp(self):
        self.class_var = iffi.SomeModel()

    def test_iffi_with_badtreshold(self):
        with patch("iffi.SomeModel.predict") as mk_var:
            mk_var.return_value = 0.2
            temp = "something text"
            self.assertEqual(type(temp), str)
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var, 0.7),
                'неуд')
            mk_var.return_value = 0.75
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var, 0.7),
                'норм')
            mk_var.return_value = 0.7
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var, 0.7),
                'норм')

            expected_calls = [mock.call("something text")] * 3
            self.assertEqual(expected_calls, mk_var.mock_calls)

    def test_iffi_with_goodtreshold(self):
        with patch("iffi.SomeModel.predict") as mk_var:
            mk_var.return_value = 0.2
            temp = "дзен пайтона"
            self.assertEqual(type(temp), str)
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var,
                                          good_thresholds=0.7),
                'неуд')
            mk_var.return_value = 0.75
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var,
                                          good_thresholds=0.7),
                'отл')
            mk_var.return_value = 0.7
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var,
                                          good_thresholds=0.7),
                'норм')

            expected_calls = [mock.call("дзен пайтона")] * 3
            self.assertEqual(expected_calls, mk_var.mock_calls)

    def test_iffi_without_bounds(self):
        with patch("iffi.SomeModel.predict") as mk_var:
            mk_var.return_value = 0.2
            temp = "набор букв"
            self.assertEqual(type(temp), str)
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var),
                'неуд')
            mk_var.return_value = 0.75
            temp = "набор 2"
            self.assertEqual(type(temp), str)
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var),
                'норм')
            mk_var.return_value = 0.8
            temp = "набор 3"
            self.assertEqual(type(temp), str)
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var, 0.7),
                'норм')
            mk_var.return_value = 0.9
            temp = "набор 4"
            self.assertEqual(type(temp), str)
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var, 0.7),
                'отл')

            expected_calls = [mock.call("набор букв"),
                              mock.call("набор 2"),
                              mock.call("набор 3"),
                              mock.call("набор 4"),
                              ]
            self.assertEqual(expected_calls, mk_var.mock_calls)

    def test_iffi_with_bounds(self):
        with patch("iffi.SomeModel.predict") as mk_var:
            mk_var.return_value = 0.2
            temp = "another text"
            self.assertEqual(type(temp), str)
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var,
                                          0.2, 0.5),
                'норм')
            mk_var.return_value = 0.75
            temp = "vk education"
            self.assertEqual(type(temp), str)
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var,
                                          0.3, 0.35),
                'отл')
            mk_var.return_value = 0.1
            temp = "набор 3"
            self.assertEqual(type(temp), str)
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var,
                                          0.2, 0.7),
                'неуд')
            mk_var.return_value = 0.9
            temp = "setter"
            self.assertEqual(type(temp), str)
            self.assertEqual(
                iffi.predict_message_mood(temp,
                                          self.class_var,
                                          0.7, 0.9),
                'норм')

            expected_calls = [mock.call("another text"),
                              mock.call("vk education"),
                              mock.call("набор 3"),
                              mock.call("setter"),
                              ]
            self.assertEqual(expected_calls, mk_var.mock_calls)
            
