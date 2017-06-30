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

    def test_assets_property_returns_all_assets(self):
        html = """
            <html>
                <head>
                    <link href="style.css"/>
                    <script src="script.js"/>
                </head>
                <body>
                    <a href="this-page.html">This Page</a>
                    <img src="smiley-face.jpg"/>
                </body>
            </html>
        """
        page_scraper = PageScraper(html)
        expected_assets = [
            'style.css',
            'script.js',
            'this-page.html',
            'smiley-face.jpg',
        ]
        
        returned_assets = page_scraper.assets

        for asset in expected_assets:
            self.assertIn(asset, returned_assets)
