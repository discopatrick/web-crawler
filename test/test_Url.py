from unittest import TestCase, skip
from source.web_crawler import *


class UrlTest(TestCase):

    def test_Url_init(self):
        url_arg = 'http://www.yoyowallet.com'

        url_object = Url(url_arg)

        self.assertEqual(url_object.url, url_arg)

    def test_Url_belongs_to_domain_returns_true_on_match(self):
        url_object = Url('http://www.bbc.co.uk/abc')

        self.assertTrue(url_object.belongs_to_domain('www.bbc.co.uk'))

    def test_Url_belongs_to_domain_returns_false_on_non_match(self):
        url_object = Url('http://www.google.co.uk/abc')

        self.assertFalse(url_object.belongs_to_domain('www.yahoo.co.uk'))

    def test_Url_get_domain(self):
        url_object = Url('http://www.amazon.co.uk/abc')

        self.assertEqual(url_object.domain, 'www.amazon.co.uk')
