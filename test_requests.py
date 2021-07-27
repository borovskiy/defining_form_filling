from app import app
import unittest


class BasicTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'http://127.0.0.1:5000/get_form?'

    def test_no_valid_response(self):
        tester = app.test_client(self)
        response = tester.post(self.url + 'f_name1=va@mail.ru&f_name2=+79503886510', content_type='html/text')
        self.assertEqual(response.json, None)

    def test_valid_response(self):
        tester = app.test_client(self)
        response = tester.post(self.url + 'f_name1=string&f_name2=+79503886510', content_type='html/text')
        self.assertEqual(type(response.json), dict)


if __name__ == '__main__':
    unittest.main()
