from unittest import TestCase, skip
from source.web_crawler import *


class UrlTest(TestCase):

    def test_Url_init(self):
        url = Url()
