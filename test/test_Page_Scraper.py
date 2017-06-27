from unittest import TestCase
from source.lib import PageScraper


class UrlTest(TestCase):

    def test_Page_Scraper_init(self):
        page_scraper = PageScraper()
