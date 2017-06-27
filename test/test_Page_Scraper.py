from unittest import TestCase
from source.lib import PageScraper


class PageScraperTest(TestCase):

    def test_Page_Scraper_init(self):
        html = """
            <html></html>
        """
        page_scraper = PageScraper(html)
