from unittest import TestCase, skip
from source.web_crawler import *


class UrlTest(TestCase):

    def test_Url_init(self):
        url_arg = 'http://www.yoyowallet.com'

        url_object = Url(url_arg)

        self.assertEqual(url_object.url, url_arg)
