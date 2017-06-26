from unittest import TestCase, skip
from source.web_crawler import *

class CrawlerTest(TestCase):

    def test_Crawler_init(self):
        start_url = 'http://www.yoyowallet.com'

        crawler = Crawler(start_url)

        self.assertIn(start_url, crawler.url_list_as_strings)

    def test_Crawler_add_url(self):
        crawler = Crawler('http://www.yoyowallet.com/')
        additional_url = 'http://www.bbc.co.uk/'

        crawler.add_url(additional_url)

        self.assertIn(additional_url, crawler.url_list_as_strings)
