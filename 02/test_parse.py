from unittest.mock import patch
from unittest import mock
import unittest
import parse


class TestParse(unittest.TestCase):
    def setUp(self) -> None:
        self.data = """{ "pets": "dog dog dog cat",
                        "owner":"mother father brother sister cat ",
                        "name":"John John Alisa Alisa",
                        "age":"50 50 20 20"}"""

    def test_parse_1(self):
        """This test also checks full match  do != dog """

        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets"], ["do", "cat"])
            self.assertEqual(mk_var.call_count, 1)
            self.assertEqual([mock.call("pets", "cat")], mk_var.mock_calls)

    def test_parse_2(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets"], ["dog"])
            self.assertEqual(mk_var.call_count, 1)
            self.assertEqual([mock.call("pets", "dog")], mk_var.mock_calls)

    def test_parse_3(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets"])
            self.assertEqual(mk_var.call_count, 0)
            self.assertEqual(mock.call(), mk_var.mock_calls)

    def test_parse_4(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets", "owner"],
                             ["dog", "mother", "cat"])
            self.assertEqual(mk_var.call_count, 4)
            expected_calls = [
                mock.call("pets", "dog"),
                mock.call("pets", "cat"),
                mock.call("owner", "mother"),
                mock.call("owner", "cat"),
            ]
            self.assertEqual(expected_calls, mk_var.mock_calls)

    def test_parse_5(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var)
            self.assertEqual(mk_var.call_count, 0)
            self.assertEqual(mock.call(), mk_var.mock_calls)

    def test_parse_6(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets", "owner"], ["mouse"])
            self.assertEqual(mk_var.call_count, 0)
            self.assertEqual(mock.call(), mk_var.mock_calls)

    def test_parse_7(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets", "owner"],
                             ["dog", "cat", "mother", "do", "ca"])
            self.assertEqual(mk_var.call_count, 4)
            expected_calls = [
                mock.call("pets", "dog"),
                mock.call("pets", "cat"),
                mock.call("owner", "cat"),
                mock.call("owner", "mother"),
            ]
            self.assertEqual(expected_calls, mk_var.mock_calls)

    def test_parse_8(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["owner"], ["moth"])
            self.assertEqual(mk_var.call_count, 0)
            self.assertEqual(mock.call(), mk_var.mock_calls)

    def test_parse_9(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["owner"])
            self.assertEqual(mk_var.call_count, 0)
            self.assertEqual(mock.call(), mk_var.mock_calls)

    def test_parse_10(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, keywords=["owner"])
            self.assertEqual(mk_var.call_count, 0)
            self.assertEqual(mock.call(), mk_var.mock_calls)

    def test_parse_11(self):
        """Test checks case when just json is passed in parse"""

        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data)
            self.assertEqual(mk_var.call_count, 0)
            self.assertEqual(mock.call(), mk_var.mock_calls)
            
