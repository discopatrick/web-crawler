from unittest import TestCase
from source.lib import PageScraper


class PageScraperTest(TestCase):

    def test_Page_Scraper_init(self):
        html = """
            <html></html>
        """
        page_scraper = PageScraper(html)

    def test_links_property_returns_all_links(self):
        html = """
            <html>
                <body>
                    <a href="this-page.html">This Page</a>
                    <a href="that-page.html">That Page</a>
                </body>
            </html>
        """
        page_scraper = PageScraper(html)
        returned_links = page_scraper.links
        expected_links = [
            'this-page.html',
            'that-page.html'
        ]
        self.assertEqual(returned_links, expected_links)
