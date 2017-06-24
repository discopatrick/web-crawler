from unittest import TestCase, skip
from source.web_crawler import *

class CrawlerTest(TestCase):

    def test_Crawler_init(self):
        crawler = Crawler()

    def test_Crawler_add_url(self):
        crawler = Crawler()
        url = 'http://www.yoyowallet.com/'

        crawler.add_url(url)
        crawler.add_url('http://www.bbc.co.uk/')

        self.assertIn(url, crawler.url_list)
