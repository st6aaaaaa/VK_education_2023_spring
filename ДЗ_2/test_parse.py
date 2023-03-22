from unittest.mock import patch
import unittest
import parse


class TestParse(unittest.TestCase):
    def setUp(self) -> None:
        self.data = """{ "pets": "dog dog dog cat",
                        "owner":"mother father brother sister cat ",
                        "name":"John John Alisa Alisa",
                        "age":"50 50 20 20"}"""

    def test_parse_1(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets"], ["dog", "cat"])
            self.assertEqual(mk_var.call_count, 2)

    def test_parse_2(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets"], ["dog"])
            self.assertEqual(mk_var.call_count, 1)

    def test_parse_3(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets"])
            self.assertEqual(mk_var.call_count, 0)

    def test_parse_4(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets", "owner"],
                             ["dog", "mother", "cat"])
            self.assertEqual(mk_var.call_count, 4)

    def test_parse_5(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var)
            self.assertEqual(mk_var.call_count, 0)

    def test_parse_6(self):
        with patch("parse.handler") as mk_var:
            parse.parse_json(self.data, mk_var, ["pets", "owner"], ["mouse"])
            self.assertEqual(mk_var.call_count, 0)
