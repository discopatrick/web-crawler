from unittest import TestCase
from source.web_crawler import *

class HttpRequestTest(TestCase):

  def test_http_request_status_code(self):
    url = 'http://www.bbc.co.uk'
    response = make_request(url)

    self.assertEqual(response.status_code, 200)

  def test_http_request_body(self):
    url = 'http://www.bbc.co.uk'
    response = make_request(url)

    self.assertIsNotNone(response.text)

  def test_bad_url(self):
    url = 'asdf'
    response = make_request(url)

    self.assertIsNone(response)
