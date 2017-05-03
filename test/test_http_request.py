from unittest import TestCase
from source.web_crawler import *

class HttpRequestTest(TestCase):

  def test_http_request(self):
    url = 'http://www.bbc.co.uk'
    response = make_request(url)

    self.assertEqual(response, 'response')
