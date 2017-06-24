from unittest import TestCase, skip
from source.web_crawler import *


class UrlTest(TestCase):

    def test_Url_init(self):
        url_arg = 'http://www.yoyowallet.com'

        url = Url(url_arg)
