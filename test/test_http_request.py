from unittest import TestCase, skip
from source.web_crawler import *


class HttpRequestTest(TestCase):

    @skip
    def test_http_request_status_code(self):
        url = 'http://www.bbc.co.uk'
        response = make_request(url)

        self.assertEqual(response.status_code, 200)

    @skip
    def test_http_request_body(self):
        url = 'http://www.bbc.co.uk'
        response = make_request(url)

        self.assertIsNotNone(response.text)

    @skip
    def test_bad_url(self):
        url = 'asdf'
        response = make_request(url)

        self.assertIsNone(response)

    @skip
    def test_https_url(self):
        url = 'https://www.bbc.co.uk'
        response = make_request(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            response.headers['content-type'].startswith('text/html'))
