from unittest import TestCase
from source.web_crawler import Crawler


class EndToEndTestCase(TestCase):

    def test_end_to_end(self):
        crawler = Crawler('http://localhost:8080/')
        expected_crawled_pages = [
            'http://localhost:8080/',
            'http://localhost:8080/that-page.html'
        ]
        expected_crawl_count = len(expected_crawled_pages)
        crawler.crawl()
        self.assertEqual(crawler.crawled_count(), expected_crawl_count)
