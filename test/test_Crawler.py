from unittest import TestCase, skip
from source.web_crawler import *

class CrawlerTest(TestCase):

    def test_Crawler_init(self):
        crawler = Crawler()

        url = 'http://www.yoyowallet.com/'
        crawler.add_url(url)
