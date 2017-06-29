from unittest import TestCase
from source.web_crawler import Crawler


class EndToEndTestCase(TestCase):

    def test_end_to_end(self):
        crawler = Crawler('http://localhost:8080/')
        crawler.crawl()
        # TODO: make this test pass (currently passes intermittently)
        self.assertEqual(crawler.crawled_count(), 1)
