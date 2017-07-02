from unittest import TestCase, skip
from source.web_crawler import *

class CrawlerTest(TestCase):

    def test_Crawler_init(self):
        start_url = 'http://www.yoyowallet.com'

        crawler = Crawler(start_url)

        self.assertIn(start_url, crawler.url_list_as_strings)

    def test_Crawler_domain(self):
        crawler = Crawler('http://www.bbc.co.uk/def')

        self.assertEqual(crawler.domain, 'www.bbc.co.uk')

    def test_Crawler_ignores_fragments(self):
        fragment_url = 'http://www.yoyowallet.com#foo'

        crawler = Crawler(fragment_url, ignore_fragment=True)

        expected_url = 'http://www.yoyowallet.com'

        self.assertIn(expected_url, crawler.url_list_as_strings)
        self.assertNotIn(fragment_url, crawler.url_list_as_strings)
